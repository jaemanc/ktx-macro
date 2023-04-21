from rest_framework import viewsets
from rest_framework import filters
from .serializers import *


class KtxUserViewSet(viewsets.ModelViewSet):
    queryset = KtxUser.objects.all()
    serializer_class = KtxUserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'phone')


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = KtxUserInfoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user_id','username','email','membership_no','dprtr_sttn','arrvl_station')

class PayCodeViewSet(viewsets.ModelViewSet):
    queryset = PayCode.objects.all()
    serializer_class = PayCodeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('code', 'name')

class UserHistoryViewSet(viewsets.ModelViewSet):
    queryset = UserHistory.objects.all()
    serializer_class = UserHistorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id','user_id','dprtr_sttn', 'arrvl_sttn', 'pay_code', 'payments')


