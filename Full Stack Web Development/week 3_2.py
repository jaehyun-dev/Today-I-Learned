import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://finance.naver.com/marketindex/?tabSel=materials#tab_section',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

# 에너지 선물
# 가스오일 #content > div:nth-child(3) > table > tbody > tr:nth-child(1)
# 난방유 #content > div:nth-child(3) > table > tbody > tr:nth-child(2)
# 천연가스 #content > div:nth-child(3) > table > tbody > tr:nth-child(3)

#content > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.tit

# 비철금속 현물
# 구리 #content > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.tit
# 구리 가격 #content > div:nth-child(4) > table > tbody > tr:nth-child(1) > td:nth-child(3)

energy = soup.select('#content > div:nth-child(3) > table > tbody > tr')
metal = soup.select('#content > div:nth-child(4) > table > tbody > tr')
agriculture = soup.select('#content > div:nth-child(5) > table > tbody > tr')

for commodity in energy:
    a_tag = commodity.select_one('td.tit')
    a_tag2 = commodity.select_one('td:nth-child(4)')
    if a_tag is not None:
        name = a_tag.text
        price = a_tag2.text
        print(name, price)

for commodity in metal:
    a_tag = commodity.select_one('td.tit')
    a_tag2 = commodity.select_one('td:nth-child(3)')
    if a_tag is not None:
        name = a_tag.text
        price = a_tag2.text
        print(name, price)

for commodity in agriculture:
    a_tag = commodity.select_one('td.tit')
    a_tag2 = commodity.select_one('td:nth-child(4)')
    if a_tag is not None:
        name = a_tag.text
        price = a_tag2.text
        print(name, price)
