from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from daisyapi.views.auth import login_user, register_user
from daisyapi.views import CocktailView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'cocktails', CocktailView, 'cocktail')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]