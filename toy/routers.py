from rest_framework import routers
from article.viewsets import ArticleViewSet
from ktxmacro.viewsets import *


router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)
router.register(r'ktxUser', KtxUserViewSet)
router.register(r'userInfo', UserInfoViewSet)
router.register(r'payCode', PayCodeViewSet)
router.register(r'userHistory', UserHistoryViewSet)
