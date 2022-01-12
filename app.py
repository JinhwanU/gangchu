from flask import Flask, render_template, jsonify, request, flash, redirect, url_for, session
from forms import LoginForm
from bson.objectid import ObjectId

app = Flask(__name__)

# CSRF(Cross-Site Request Forgery) 보호하기 위해 사용
# WTForms 라이브러리 사용 시 필수적으로 포함되어야 한다
# secrets import 후 secrets.token_hex(16) 해시함수 사용하여 토큰 생성
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.gangchu


def gi(name):
    temp = list(db.review.find({'title':name},))
    cnt = 0;
    for i in temp:
        rating = int(i['rating'])
        cnt += rating
    if cnt == 0:
        aver = '없음'
    else:
        aver =round(cnt / len(temp),2)
    db.classlist.update_one({'title': name}, {'$set':{"aver":aver} },False,True)

# HTML 화면 보여주기
@app.route('/')
def home():
    temp = list(db.classlist.find({}))
    for h in temp:
        insert = h['title']
        gi(insert);
    return render_template('main.html')


@app.route('/readList', methods=['GET'])
def read_list():
    class_list = list(db.classlist.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'class_list': class_list})


@app.route('/map')
def route_map():
    return render_template('map.html')


@app.route('/board', methods=['get'])
def route_board():
    title_receive = request.args.get('title')
    img_receive = db.classlist.find_one({'title':title_receive})
    img_url = img_receive['img_url']
    return render_template('board.html', title = title_receive,img_url=img_url)

@app.route('/readBoard', methods=['get'])
def read_review():
    title_receive = request.args.get('title')
    mongo_list = db.review.find({'title':title_receive})
    sec_id = []
    for id_list in mongo_list:
        id_list['_id'] = str(id_list['_id'])
        sec_id.append(id_list)

    review_list = list(db.review.find({'title':title_receive}, {'_id': False}))
    return jsonify({'review_list': review_list,'sec_id':sec_id, 'result': 'success'})

@app.route('/deleteBoard', methods=['POST'])
def delete_review():

    id_receive = request.form["id_give"]
    db.review.delete_one({'_id': ObjectId(id_receive)})
    return jsonify({'result': 'success'})

@app.route('/updateBoard', methods=['POST'])
def update_review():
    id_receive = request.form["id_give"]
    review_receive = request.form["review_give"]
    db.review.update_one({'_id': ObjectId(id_receive)}, {'$set': {'review': review_receive}})
    return jsonify({'result': 'success'})

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
