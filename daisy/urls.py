from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from daisyapi.views.auth import login_user, register_user
from daisyapi.views import CocktailView
from daisyapi.views.cocktail_ingredient import CocktailIngredientView
from daisyapi.views.glass import GlassView
from daisyapi.views.ice import IceView
from daisyapi.views.ingredient_types import IngredientTypeView
from daisyapi.views.ingredients import IngredientView
from daisyapi.views.preparations import PreparationView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'cocktails', CocktailView, 'cocktail')
router.register(r'cocktail_ingredients', CocktailIngredientView, 'cocktail_ingredient')
router.register(r'ingredients', IngredientView, 'ingredient')
router.register(r'ingredient_types', IngredientTypeView, 'ingredient_types')
router.register(r'preparations', PreparationView, 'preparation')
router.register(r'ice', IceView, 'ice')
router.register(r'glass', GlassView, 'glass')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]