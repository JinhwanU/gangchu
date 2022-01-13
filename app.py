from flask import Flask, render_template, jsonify, request, flash, redirect, url_for, session
from forms import LoginForm

app = Flask(__name__)

# CSRF(Cross-Site Request Forgery) 보호하기 위해 사용
# WTForms 라이브러리 사용 시 필수적으로 포함되어야 한다
# secrets import 후 secrets.token_hex(16) 해시함수 사용하여 토큰 생성
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.gangchu


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('main.html')


@app.route('/readList', methods=['GET'])
def read_list():
    class_list = list(db.classlist.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'class_list': class_list})


@app.route('/map')
def route_map():
    return render_template('map.html')

#############################################################
###이기녕 app.py

@app.route('/api/maplist', methods=["GET"])
def get_map():
    # 학원 목록을 반환하는 API
    # 1. 데이터 베이스에서 학원 목록을 꺼내와야 한다.
    aca_list = list(db.shops.find({}, {'_id': False}))
    # aca_list 라는 키 값에 학원 목록을 담아 클라이언트에게 반환합니다.
    # 2. 그걸 클라이언트에 돌려준다
    return jsonify({'result': 'success', 'aca_list': aca_list})

@app.route('/like_academy', methods=["POST"])
def like_aca():
    title_receive = request.form["title_give"]
    address_receive = request.form["address_give"]
    action_receive = request.form["action_give"]
    print(title_receive, address_receive, action_receive)

    if action_receive == "like":
        db.shops.update_one({"title": title_receive, "address": address_receive}, {"$set": {"liked": True}})
    else:
        db.shops.update_one({"title": title_receive, "address": address_receive}, {"$unset": {"liked": False}})
    return jsonify({'result': 'success'})

#############################################################
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
    # False일 경우 회원가입 페이지로 돌아감
    # True일 경우 flash메세지 보낸 후 redirect (main.html: 메세지 획득 후 alert 실행)
    # DB관련 작업 추가 예정
    if request.method == 'POST':
        if (form.validate() == False):
            return render_template('login.html', form=form)
        else:
            flash(f'{form.username.data}님 환영합니다')
            return redirect(url_for("home"))


        # user = User.query.filter_by(username=form.username.data).first()
        # if not user:
        #     user = User(username=form.username.data,
        #                 password=generate_password_hash(form.password1.data),
        #                 email=form.email.data)
        #     db.session.add(user)
        #     db.session.commit()
        #     return redirect(url_for('main.index'))
        # else:
        #     flash('이미 존재하는 사용자입니다.')
    return render_template('login.html', form=form)


@app.route('/login/<signup>', methods=["GET", "POST"])
def route_signup(signup):
    signup_form = LoginForm()
    if request.method == 'POST':
        if (signup_form.validate() == False):
            return render_template('login.html', form=signup_form, login_form='signup')
        else:
            flash(f'{signup_form.username.data}님 환영합니다')
            return redirect(url_for("home"))
    return render_template('login.html', form=signup_form, login_form=signup)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
