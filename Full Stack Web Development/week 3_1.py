import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    img_tag = tr.select_one('img')
    a_tag = tr.select_one('td.title > div > a')
    point_tag = tr.select_one('td.point')
    if a_tag is not None:
        rank = img_tag['alt']
        title = a_tag.text
        point = point_tag.text
        print(rank, title, point)
