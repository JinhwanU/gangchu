import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
client = MongoClient('localhost', 27017)
db = client.gangchu
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

<<<<<<< Updated upstream
# 스파르타 코딩클럽의 온라인 강의의 이미지와 설명 그리고 강의명을 크롤링해 DB에 저장한다.
def addonline(adress):
    # 카탈로그의 필드값을 기준으로 잡고 여러 필드를 대입해 각 필드의 강의를 크롤링한다.
=======

def addonline(adress):
>>>>>>> Stashed changes
    data = requests.get('https://spartacodingclub.kr/catalog/field/'+adress, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    d = soup.select('#catalog_course_pkg_content > div > div.wrapper__bundles > div')
    cnt = 1
    cnt1 = 1
    for i in d:
        a_tag = i.select('div.wrapper__bundles__bundle__courses > div')
        cnt = cnt + 1
        cnt1 = 1
        for o in a_tag:
<<<<<<< Updated upstream
            # 각페이지의 이미지과 설명을 크롤링후 강의명을 크롤링하기위해 상세페이지로 들어간다.
=======
>>>>>>> Stashed changes
            b_tag = o.select_one('img')['src']
            c_tag = o.select_one('div.wrapper__bundles__bundle__courses__course__desc').get_text()
            e_tag = o['data-url']
            url = 'https://spartacodingclub.kr/' + e_tag
            data = requests.get(url, headers=headers)
            soup = BeautifulSoup(data.text, 'html.parser')
            d_tag = soup.select_one('#curri_detail_title > div > h1')
<<<<<<< Updated upstream
            # 상세페이지별로 강의명의 위치가 달라서 3개의 if 문으로 강의명을 받는다.
=======
>>>>>>> Stashed changes
            if d_tag != None:
                f_tag = d_tag.text
            else:
                d_tag = soup.select_one(
                    '#tmt_curri_detail_hero > div.tmt_curri_detail_hero__text > div.tmt_curri_detail_hero__text__title > div.tmt_curri_detail_hero__text__title__info')
                if d_tag != None:
                    f_tag = d_tag.text.strip()[:-4]
                else:
                    d_tag = soup.select_one('#wrap > section.t_area > div.tx > h2')
                    if d_tag != None:
                        f_tag = d_tag.text
                    else:
                        d_tag = soup.select_one('#maker_curri_detail_hero_info > div > h1')
                        f_tag = d_tag.text
<<<<<<< Updated upstream
            # 받은 데이터를 도큐먼트화 시키고 텍스트의 필요한 부분만 저장한다.
=======
>>>>>>> Stashed changes
            doc = {
                'img_url': b_tag,
                'text': c_tag,
                'title': f_tag[:-4],
                'url': url
            }
<<<<<<< Updated upstream
            # 뷰티풀 스푼의 위치를 다시 메인페이지로 이동시킨다.
            db.classlist.insert_one(doc)
=======
            db.mystar.insert_one(doc)
>>>>>>> Stashed changes
            data = requests.get('https://spartacodingclub.kr/catalog/field/' + adress, headers=headers)
            soup = BeautifulSoup(data.text, 'html.parser')
            cnt1 = cnt1 + 1

<<<<<<< Updated upstream
# 스파르타 코딩클럽의 필드종류를 묶어 db저장 함수에 집어넣는다.
list = ['web','app','grammar','datascience','game']
db.classlist.drop()
=======

list = ['web','app','grammar','datascience','game']
db.mystar.drop()
>>>>>>> Stashed changes
for x in list:
    addonline(x)