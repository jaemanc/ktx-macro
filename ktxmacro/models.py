from django.db import models


class KtxUser(models.Model):
    id = models.CharField(primary_key=True, max_length=40, null=False, blank=True)
    pwd = models.CharField(max_length=40, null=False, blank=True)
    phone = models.CharField(max_length=12, null=False, blank=True, db_index=True)
    creation_date = models.CharField(max_length=50, default='-1')

    class Meta:
        db_table = 'ktx_user'


class UserInfo(models.Model):
    user_id = models.CharField(max_length=30, null=False, blank=True, db_index=True)
    username = models.CharField(max_length=30, null=False, blank=True, db_index=True)
    email = models.CharField(max_length=50, null=False, blank=True, db_index=True)
    membership_no = models.CharField(max_length=30, null=False, blank=True, db_index=True)
    dflt_dprtr_sttn = models.CharField(max_length=15, null=False, blank=True, db_index=True) # 기본 출발역 세팅
    dflt_arrvl_sttn = models.CharField(max_length=15, null=False, blank=True, db_index=True) # 기본 도착역 세팅
    pay_code = models.CharField(max_length=10, null=False, blank=True)

    class Meta:
        db_table = 'ktx_user_info'


class PayCode(models.Model):
    code = models.CharField(max_length=20, null=False, blank=True, db_index=True)
    name = models.CharField(max_length=30, null=False, blank=True, db_index=True)
    expl = models.CharField(max_length=100, null=False, blank=True, db_index=True)

    class Meta:
        db_table = 'paycode'


class UserHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=30, null=False, blank=True, db_index=True)
    dprtr_sttn = models.CharField(max_length=15, null=False, blank=True, db_index=True)
    arrvl_sttn = models.CharField(max_length=15, null=False, blank=True, db_index=True)
    pay_code = models.CharField(max_length=10, null=False, blank=True)
    payments = models.IntegerField(null=False, blank=True)  # 금액
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'user_history'
