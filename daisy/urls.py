from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from daisyapi.views.auth import login_user, register_user
from daisyapi.views import CocktailView
from daisyapi.views.cocktail_ingredient import CocktailIngredientView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'cocktails', CocktailView, 'cocktail')
router.register(r'cocktail_ingredients', CocktailIngredientView, 'cocktail_ingredient')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]