import hashlib

import jwt
from datetime import datetime, timedelta
from flask import Flask, render_template, jsonify, request, flash, redirect, url_for

from forms import LoginForm, SignupForm

app = Flask(__name__)

# CSRF(Cross-Site Request Forgery) 보호하기 위해 사용
# WTForms 라이브러리 사용 시 필수적으로 포함되어야 한다
# secrets import 후 secrets.token_hex(16) 해시함수 사용하여 토큰 생성
app.config["SECRET_KEY"] = 'sparta'
SECRET_KEY = "sparta"

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.gangchu


# HTML 화면 보여주기
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"id": payload["id"]})
        # print(user_info)
        return render_template('main.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("route_login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("route_login", msg="로그인 정보가 존재하지 않습니다."))
    # return render_template('main.html')


@app.route('/readList', methods=['GET'])
def read_list():
    class_list = list(db.classlist.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'class_list': class_list})


@app.route('/map')
def route_map():
    return render_template('map.html')


@app.route('/board')
def route_board():
    title_receive = request.args.get('title')
    review_list = list(db.review.find({'title': title_receive}, {'_id': False}))
    return render_template('board.html', review_list=review_list, title=title_receive)


@app.route('/writeBoard', methods=['POST'])
def write_review():
    # 1. 클라이언트로부터 데이터를 받기
    id_receive = request.form["id_give"]
    rating_receive = request.form["rating_give"]
    review_receive = request.form["review_give"]
    title_receive = request.form["title_give"]
    doc = {
        'id': id_receive, 'rating': rating_receive,
        'title': title_receive, 'review': review_receive,
    }
    db.review.insert_one(doc)

    return jsonify({'result': 'success'})


@app.route('/mypage')
def route_mypage():
    return render_template('mypage.html')


@app.route("/login", methods=["GET", "POST"])
def route_login():
    # forms에 선언한 RegistrationForm클래스의 자식 객체 생성
    form = LoginForm()

    # POST방식으로 호출한 경우 유효성 검증
    if request.method == 'POST':
        if not form.validate():
            return render_template('login.html', form=form)

        # 로그인 검증
        else:
            receive_id = form.userID.data
            receive_pw = form.password.data
            password_hash = hashlib.sha256(receive_pw.encode('utf-8')).hexdigest()

            result = db.users.find_one({'id': receive_id, 'password': password_hash})

            # 로그인 성공
            if result is not None:
                payload = {'id': receive_id, 'exp': datetime.utcnow() + timedelta(hours=1)}  # 로그인 1시간 유지
                token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                # print(token)
                # token_decode = jwt.decode(token, SECRET_KEY, 'HS256')
                # token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                return render_template("main.html", token=token)

            # 로그인 실패
            else:
                flash('아이디와 패스워드를 확인해주세요')
                return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@app.route('/login/<signup>', methods=["GET", "POST"])
def route_signup(signup):
    form = SignupForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('login.html', form=form, login_form=signup)
        else:
            duplic_id = db.users.find_one({'id': form.userID.data}, {'_id': False, 'id': 1})
            duplic_email = db.users.find_one({'email': form.email.data}, {'_id': False, 'email': 1})
            duplic_check = [duplic_id, duplic_email]

            # None 필터링
        result = list(filter(None, duplic_check))

        # 중복 검사 ( result에 값이 존재하면 if문 내부 진입 )
        if result:
            for i in result:
                key = list(i.keys())
                flash(f'이미 사용된 {key} 입니다.')
            return render_template('login.html', form=form, login_form=signup)

        # 회원가입 성공(DB에 저장)
        else:
            # 비밀번호 암호화(hash)
            password_hash = hashlib.sha256(form.password.data.encode('utf-8')).hexdigest()
            doc = {
                'id': form.userID.data, 'email': form.email.data, 'password': password_hash
            }
            db.users.insert_one(doc)
            flash(f'{form.userID.data}님 환영합니다. 로그인 후 이용해주세요')
            return redirect(url_for("home"))

    return render_template('login.html', form=form, login_form=signup)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
