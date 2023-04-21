import json
import logging
import traceback

from ktxmacro.models import UserInfo
from rest_framework.response import Response
from rest_framework import mixins, status, viewsets
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from ktxmacro.serializers import KtxUserInfoSerializer

logger = logging.getLogger()


class ktx_user_info_api(viewsets.GenericViewSet, mixins.ListModelMixin, View):
    def get_ktx_user_info(self, request):

        userInfo = None

        try:
            # localhost:8765/ktx/user?user_id=test123
            logger.debug(f'url: ktx/user?user_id=<user_id>')
            logger.debug(f'method: get')
            logger.debug(f'request_query_param:  {request.GET}')
            userInfo = get_ktx_user_info(request)

            if userInfo is None:
                return Response(
                    {
                        'message': 'MODEL NOT FOUNDED',
                        'data': None
                    }, status=status.HTTP_204_NO_CONTENT)

            return Response(data=userInfo, status=status.HTTP_200_OK)

        except Exception as ex:
            logger.debug(f'url: ktx/user?user_id=<user_id> getKtxUserInfo() Error: {traceback.format_exc()}')
            traceback.print_exc()
            return Response(
                {
                    'message': 'success',
                    'data': userInfo.data
                }, status=status.HTTP_204_NO_CONTENT)

    def register(self, request):
        userInfo = None
        try:
            logger.debug(f'url: ktx/user/register')
            logger.debug(f'method: post')
            logger.debug(f'request_data: {request.body}')

            # 유효성 검증.
            if not is_validate(request):
                return Response(data=None, status=status.HTTP_409_CONFLICT)

            # ktx_user 테이블 체크 .
            # get_ktx_user(request)

            # user_info 등록.
            userInfo = register(request)

            return Response(data=userInfo, status=status.HTTP_201_CREATED)

        except Exception as ex:
            logger.debug(f'url: ktx/user?user_id=<user_id> getKtxUserInfo() Error: {traceback.format_exc()}')
            traceback.print_exc()
            return Response(data=None, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_ktx_user_info(request):
    userInfo = None

    userInfo = UserInfo.objects.get(user_id=request.GET.get('user_id'))

    if not userInfo:
        return None

    userInfo = KtxUserInfoSerializer(userInfo)
    logger.debug(f"get_ktx_user_info param {request.GET.get('user_id')} userInfo")

    return userInfo.data


def is_validate(request):

    flag = True

    req_body = json.loads(request.body)

    try:
        if UserInfo.objects.get(user_id=req_body['user_id']) is not None:
            flag = False

    except ObjectDoesNotExist:
        pass

    return flag


def register(request):
    userInfo = None
    req_body = json.loads(request.body)
    logger.debug(f'register data : {req_body}')

    UserInfo.objects.create(
        user_id=req_body['user_id'],
        username=req_body['username'],
        email=req_body['email'],
        membership_no=req_body['membership_no'],
        dflt_dprtr_sttn=req_body['dflt_dprtr_sttn'],
        dflt_arrvl_sttn=req_body['dflt_arrvl_sttn'],
        pay_code=req_body['pay_code']
    )

    userInfo = UserInfo.objects.get(user_id=req_body['user_id'])
    userInfo = KtxUserInfoSerializer(userInfo)

    return userInfo.data


