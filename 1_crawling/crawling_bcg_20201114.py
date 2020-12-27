import re

import requests
from bs4 import BeautifulSoup

# 네이버 매출정보 크롤링 ###
rq_naver = requests.get(
    "http://dart.fss.or.kr/report/viewer.do?rcpNo=20200814001974&dcmNo=7446945&eleId=10&offset=177077&length=157288&dtd=dart3.xsd")
result_naver = rq_naver.content
soup = BeautifulSoup(result_naver, "html.parser")
naver = str(soup.find_all("tr"))
naver = re.sub('<.+?>', '', naver, 0).strip()
fd = open("naver.csv", "w", encoding='utf-8')
fd.write(naver)
print(naver)


# 네이버 2016년도 매출정보 크롤링 #
rq_naver_2016 = requests.get(
    "http://dart.fss.or.kr/report/viewer.do?rcpNo=20160816002079&dcmNo=5262442&eleId=10&offset=129708&length=132448&dtd=dart3.xsd")
result_naver_2016 = rq_naver_2016.content
soup = BeautifulSoup(result_naver_2016, "html.parser")
naver_2016 = str(soup.find_all("tr"))
naver_2016 = re.sub('<.+?>', '', naver_2016, 0).strip()
fd = open("naver_2016.csv", "w", encoding='utf-8')
fd.write(naver_2016)
print(naver_2016)

# 카카오 매출정보 크롤링 #
rq_kakao = requests.get(
    "http://dart.fss.or.kr/report/viewer.do?rcpNo=20200814002188&dcmNo=7447711&eleId=10&offset=287158&length=197448&dtd=dart3.xsd")
result_kakao = rq_kakao.content
soup = BeautifulSoup(result_kakao, "html.parser")
kakao = str(soup.find_all("tr"))
kakao = re.sub('<.+?>', '', kakao, 0).strip()
fd = open("kakao.csv", "w", encoding='utf-8')
fd.write(kakao)
print(kakao)

# 카카오 2016년도 매출정보 크롤링 #
rq_kakao_2016 = requests.get(
    "http://dart.fss.or.kr/report/viewer.do?rcpNo=20160816002028&dcmNo=5262283&eleId=10&offset=271961&length=146730&dtd=dart3.xsd")
result_kakao_2016 = rq_kakao_2016.content
soup = BeautifulSoup(result_kakao_2016, "html.parser")
kakao_2016 = str(soup.find_all("tr"))
kakao_2016 = re.sub('<.+?>', '', kakao_2016, 0).strip()
fd = open("kakao_2016.csv", "w", encoding='utf-8')
fd.write(kakao_2016)
print(kakao_2016)