import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.gangchu
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


def addonline(adress):
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
            b_tag = o.select_one('img')['src']
            c_tag = o.select_one('div.wrapper__bundles__bundle__courses__course__desc').get_text()
            e_tag = o['data-url']
            url = 'https://spartacodingclub.kr/' + e_tag
            data = requests.get(url, headers=headers)
            soup = BeautifulSoup(data.text, 'html.parser')
            d_tag = soup.select_one('#curri_detail_title > div > h1')
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
            doc = {
                'img_url': b_tag,
                'text': c_tag,
                'title': f_tag[:-4],
                'url': url
            }
            db.classlist.insert_one(doc)
            data = requests.get('https://spartacodingclub.kr/catalog/field/' + adress, headers=headers)
            soup = BeautifulSoup(data.text, 'html.parser')
            cnt1 = cnt1 + 1


list = ['web','app','grammar','datascience','game']
db.classlist.drop()
for x in list:
    addonline(x)