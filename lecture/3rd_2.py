import requests
from datetime import datetime

from bs4 import BeautifulSoup


# today = datetime.today()
today = datetime.now().strftime('%Y%m%d')


# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
for page in range(1,4):
    data = requests.get(f'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date={today}&page={page}',headers=headers)
    # data = requests.get(f'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303&page={page}',headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
    # 이제 코딩을 통해 필요한 부분을 추출하면 된다.
    soup = BeautifulSoup(data.text, 'html.parser')

    # select를 이용해서, tr들을 불러오기
    movies = soup.select('#old_content > table > tbody > tr')

    # movies (tr들) 의 반복문을 돌리기
    for movie in movies:
        # movie 안에 a 가 있으면,
        
        #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
        a_tag = movie.select_one('td.title > div > a')
        #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
        point = movie.select_one('td.point')
        if page == 1:
            rank = movie.select_one('td:nth-child(1) > img')
            if rank is not None:
                rank = rank['alt']
        else:
            rank = movie.select_one('td.order')
            if rank is not None:
                rank = rank.text
            #old_content > table > tbody > tr:nth-child(2) > td.order
        if a_tag is not None:

            # a의 text를 찍어본다.
            # print (f'{i:02}', a_tag.text, point.text)
            print (rank, a_tag.text, point.text)