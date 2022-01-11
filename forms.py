from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("아이디", validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField("이메일", validators=[DataRequired(), Email("올바른 형식의 이메일을 입력해주세요")])
    password = PasswordField("비밀번호", validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField("비밀번호 확인", validators=[DataRequired(), EqualTo("password","비밀번호가 일치하지 않습니다")])
    submit = SubmitField("가입")
