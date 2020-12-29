import re

import requests
from bs4 import BeautifulSoup

# SKTelecom 매출정보 크롤링 ###
rq_skt = requests.get(
    "http://dart.fss.or.kr//report/viewer.do?rcpNo=20200814002234&dcmNo=7447875&eleId=10&offset=238426&length=186047&dtd=dart3.xsd")
result_skt = rq_skt .content
soup = BeautifulSoup(result_skt , "html.parser")
skt = str(soup.find_all("tr"))
skt = re.sub('<.+?>', '', skt, 0).strip()
fd = open("skt.csv", "w", encoding='utf-8')
fd.write(skt)
print(skt)


# SKTelecom 2016년도 매출정보 크롤링 #
rq_skt_2016 = requests.get(
    "http://dart.fss.or.kr/report/viewer.do?rcpNo=20150817001521&dcmNo=4772310&eleId=10&offset=156994&length=150220&dtd=dart3.xsd")
result_skt_2016 = rq_skt_2016.content
soup = BeautifulSoup(result_skt_2016, "html.parser")
skt_2016 = str(soup.find_all("tr"))
skt_2016 = re.sub('<.+?>', '', skt_2016, 0).strip()
fd = open("skt_2016.csv", "w", encoding='utf-8')
fd.write(skt_2016)
print(skt_2016)

# KT 매출정보 크롤링 #
rq_kt = requests.get(
    "http://dart.fss.or.kr//report/viewer.do?rcpNo=20200814002766&dcmNo=7449734&eleId=10&offset=171014&length=504655&dtd=dart3.xsd")
result_kt = rq_kt.content
soup = BeautifulSoup(result_kt, "html.parser")
kt = str(soup.find_all("tr"))
kt = re.sub('<.+?>', '', kt, 0).strip()
fd = open("kt.csv", "w", encoding='utf-8')
fd.write(kt)
print(kt)

# KT 2016년도 매출정보 크롤링 #
rq_kt_2016 = requests.get(
    "http://dart.fss.or.kr/report/viewer.do?rcpNo=20150817001642&dcmNo=4772741&eleId=10&offset=182539&length=1075589&dtd=dart3.xsd")
result_kt_2016 = rq_kt_2016.content
soup = BeautifulSoup(result_kt_2016, "html.parser")
kt_2016 = str(soup.find_all("tr"))
kt_2016 = re.sub('<.+?>', '', kt_2016, 0).strip()
fd = open("kt_2016.csv", "w", encoding='utf-8')
fd.write(kt_2016)
print(kt_2016)

# LGU+ 2020년도 매출정보 크롤링 #
rq_lgu = requests.get(
    "http://dart.fss.or.kr/report/viewer.do?rcpNo=20200814002424&dcmNo=7448513&eleId=10&offset=234694&length=399270&dtd=dart3.xsd")
result_lgu = rq_lgu.content
soup = BeautifulSoup(result_lgu, "html.parser")
lgu = str(soup.find_all("tr"))
lgu = re.sub('<.+?>', '', lgu, 0).strip()
fd = open("lgu.csv", "w", encoding='utf-8')
fd.write(lgu)
print(lgu)

# LGU 2016년도 매출정보 크롤링 #
rq_lgu_2016 = requests.get(
    "http://dart.fss.or.kr/report/viewer.do?rcpNo=20150813000987&dcmNo=4765409&eleId=10&offset=197003&length=263377&dtd=dart3.xsd")
result_lgu_2016 = rq_lgu_2016.content
soup = BeautifulSoup(result_lgu_2016, "html.parser")
lgu_2016 = str(soup.find_all("tr"))
lgu_2016 = re.sub('<.+?>', '', lgu_2016, 0).strip()
fd = open("lgu_2016.csv", "w", encoding='utf-8')
fd.write(lgu_2016)
print(lgu_2016)