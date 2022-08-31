from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from daisyapi.views.auth import login_user, register_user

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]
