from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp


# WTForms 라이브러리를 이용하여 회원가입/로그인 유효성 검증
class LoginForm(FlaskForm):
    userID = StringField("아이디", validators=[DataRequired(), Length(min=4, max=20),
                                              Regexp("(^[A-Za-z]+\w)", message="ID : 대·소문자로 시작, 대·소문자,숫자 입력")])
    email = StringField("이메일", validators=[DataRequired(), Email("올바른 형식의 이메일을 입력해주세요")])
    password = PasswordField("비밀번호", validators=[DataRequired(), Length(min=4, max=20),
                                                 Regexp("([A-Za-z0-9!@#$%^&*])",
                                                        message="PW : 대·소문자,숫자,특수문자(!@#$%^&*) 입력")])
    confirm_password = PasswordField("비밀번호 확인", validators=[DataRequired(), EqualTo("password", "비밀번호가 일치하지 않습니다")])
    signup_btn = SubmitField("가입")
    login_btn = SubmitField("로그인")
