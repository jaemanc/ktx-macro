from rest_framework import serializers
from ktxmacro.models import KtxUser
from ktxmacro.models import UserInfo
from ktxmacro.models import PayCode
from ktxmacro.models import UserHistory


class KtxUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = KtxUser
        fields = '__all__'


class KtxUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class PayCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayCode
        fields = '__all__'


class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = '__all__'
