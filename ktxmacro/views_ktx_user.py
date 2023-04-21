import logging
import traceback

from ktxmacro.models import UserInfo
from rest_framework.response import Response
from rest_framework import mixins, status, viewsets
from django.views import View
from ktxmacro.serializers import KtxUserInfoSerializer
from ktxmacro.serializers import KtxUserSerializer
from ktxmacro.models import KtxUser



logger = logging.getLogger()


class ktx_user_api(viewsets.GenericViewSet, mixins.ListModelMixin, View):

    queryset = KtxUser.objects.all()
    _ktx_usr_srlzr = KtxUserSerializer

    def create_ktx_user(self, request):
        self.perform_create(self, _ktx_usr_srlzr)

        return Response(None, status.HTTP_201_CREATED)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


