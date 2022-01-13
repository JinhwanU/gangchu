from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.gangchu
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

def monngo():
    temp1 = list(db.acaedmy.find({}, ))

    for i in temp1:
        temp2 = i['title']
        temp3 = list(db.acaedmy.find({'title':temp2}))
        h = 2
        while h <len(temp3)-1:
            db.acaedmy.delete_one({'title':temp2})
            h = h+1


monngo()