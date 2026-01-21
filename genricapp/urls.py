from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

"""router = DefaultRouter()
router.register('genric', StudentClass)"""

router = DefaultRouter()
router.register('allgenric', StudentGenricClass )


urlpatterns = [
    path ('', include(router.urls)),
    path('login/',obtain_auth_token)
    

]