import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

avengers = db.movies.find_one({"title": '어벤져스: 엔드게임'})
same_stars = list(db.movies.find({'star' : avengers['star']},{'_id' : False}))

for movie in same_stars:
    print(movie)

db.movies.update_many({'star' :avengers['star']}, {'$set': {'star':0}})




