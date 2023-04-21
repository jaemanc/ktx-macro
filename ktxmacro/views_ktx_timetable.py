import json
import logging
import traceback

from rest_framework.response import Response
from rest_framework import mixins, status, viewsets
from django.views import View
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # 페이지 로딩 대기용


logger = logging.getLogger()


class ktx_timetable_api(viewsets.GenericViewSet, mixins.ListModelMixin, View):
    def get_ktx_timetable(self, request):

        try:
            logger.debug(f'url: ktx-timetable')
            logger.debug(f'method: get')
            logger.debug(f'request_query_param:  {request.GET}')
            # 날짜, 도착역/출발역 / 인원 검증
            flag = is_cheked(self, request)

            if not flag :
                return Response(data=None, status=status.HTTP_400_BAD_REQUEST)

            ktx_crawler(self, request)

            return Response(data=None, status=status.HTTP_200_OK)
        except Exception as ex:
            logger.debug(f'url: ktx-timetable ktx_crawler Error: {traceback.format_exc()}')
            traceback.print_exc()
            return Response({

            }, status=status.HTTP_204_NO_CONTENT)


def is_cheked(self, request):
    flag = True

    # 날짜
    if request.GET.get('date') is None:
        flag = False

    # 인원
    if request.GET.get('req_numb') is None:
        flag = False

    # 출발역
    if request.GET.get('dprtr_sttn') is None:
        flag = False

    # 도착역
    if request.GET.get('arrvl_sttn') is None:
        flag = False

    return flag


def ktx_crawler(self, request):

    req = requests.get('https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do')

    ## HTML 소스 가져오기
    html = req.text
    ## HTTP Header 가져오기
    header = req.headers
    ## HTTP Status 가져오기 (200: 정상)
    status = req.status_code
    ## HTTP가 정상적으로 되었는지 (True/False)
    is_ok = req.ok

    logger.debug(f'{is_ok} , {status}, {header}, {html}')

    driver = webdriver.Chrome('chromedriver')

    driver.get('https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do')
    time.sleep(3)


    return None

