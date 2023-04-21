#parser.py
import requests

## HTTP GET Request
req = requests.get('https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do')

## html 소스 가져오기
html = req.text

## header 가져오기
header = req.headers

# http status 가져오기
status = req.status_code

# 정상 여부 체크 ( True / False )
is_ok = req.ok



