# STUDY STARTER

스파르타 코딩클럽 강의 평가 및 리뷰와 오프라인 코딩학원의 리뷰를 공유합니다.

## 1. 제작 기간 & 팀원 소개

- 2022.01.10 ~ 01.13
- 3인 1조 팀 프로젝트


유진환 - JWT 로그인 + 마이페이지 + jinja2관련 ( login/signup/mypage.html)

이기녕 - 네이버지도 + 크롤링(셀레니움사용-네이버지도 이용한 학원 정보 크롤링) (map.html)

조상현 - 리뷰게시판 + 크롤링(스파르타 코딩클럽) (main/board.html)


## 2. 사용 기술

- `Backend`
   - Python 3
   - Flask 2.0.1
   - flask
   - flask-WTF
   - WTForms
   - email-validator
   - jwt
- `Frontend`
   - jinja
   - bootstrap
- `DB`
   - MongoDB
   - selenium


## 3. 실행화면

## 4. 핵심기능

- 로그인, 회원가입
   - JWT를 이용하여 로그인과 회원가입을 구현하였습니다.
   - 아이디와 닉네임의 중복확인이 가능합니다.

- 오프라인 코딩학원 지역별 검색
   - 크롤링을 통해 서울지역 내 코딩학원들을 DB에 미리 저장하였습니다.
   
- 1개의 강의 및 학원에 대한 리뷰글 CRUD
   - 자신의 생각을 담아 리뷰글을 작성가능합니다.
   - 다른 유저의 리뷰글을 조회할 수 있습니다.
   - 권한인증을 통하여, 자신의 리뷰글을 수정가능하며, 다른 유저의 리뷰글은 수정이 불가능합니다.
   - 권한인증을 통하여, 자신의 리뷰글을 삭제가능하며, 다른 유저의 리뷰글은 삭제가 불가능합니다.
   
## 5. 해결한 문제 정리해보기



© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
