"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from daisyapi.models import Cocktail
from daisyapi.models import Glass, Ice, Preparation
from daisyapi.models.cocktail_ingredient import CocktailIngredient
# from daisyapi.models.favorite import Favorite
from daisyapi.models.mixologist import Mixologist
from daisyapi.models.ingredient import Ingredient
from daisyapi.models.unit import Unit
from daisyapi.views.cocktail_ingredient import CocktailIngredientSerializer


class CocktailView(ViewSet):
    """Daisy cocktail view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single cocktail

        Returns:
            Response -- JSON serialized cocktail
        """
        
        try:
            cocktail = Cocktail.objects.get(pk=pk)
            serializer = CocktailSerializer(cocktail)
            return Response(serializer.data)
        except Cocktail.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    

    def list(self, request):
        """Handle GET requests to get all cocktails

        Returns:
            Response -- JSON serialized list of cocktails
        """
        
        cocktails = Cocktail.objects.all().order_by('name')
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)
    
    # def filter_by_favorite(self, request, pk):
    #     """Get request to filter by favorite cocktails """
    #     mixologist = Mixologist.objects.get(user=request.auth.user)
    #     favorites = Favorite.objects.filter(mixologist=mixologist)
    #     favorite_cocktails = [favorite.cocktail for favorite in favorites]
    #     serializer = CocktailSerializer(favorite_cocktails, many=True)
    #     return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized cocktail instance
        """
        creator = Mixologist.objects.get(user=request.auth.user)
        ingredients = request.data.get('ingredients')
        serializer = CreateCocktailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cocktail = serializer.save(creator=creator)
        res_serializer = CocktailSerializer(cocktail)
        new_cocktail = Cocktail.objects.get(pk=serializer.data['id'])
        if ingredients:
            for data_ingredient in ingredients:
                unit_obj = Unit.objects.get(pk=data_ingredient['unit'])
                ing_obj = Ingredient.objects.get(pk=data_ingredient['ingredient'])
                cocktail_serializer = CocktailIngredientSerializer(data=data_ingredient)
                cocktail_serializer.is_valid(raise_exception=True)
                cocktail_ingredient = cocktail_serializer.save(cocktail=new_cocktail,ingredient=ing_obj, unit=unit_obj)
                cocktail_res_serializer = CocktailIngredientSerializer(cocktail_ingredient)
        return Response(res_serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a cocktail

        Returns:
            Response -- Empty body with 204 status code
        """
        
        cocktail = Cocktail.objects.get(pk=pk)
        ice = Ice.objects.get(pk=request.data['ice'])
        glass = Glass.objects.get(pk=request.data['glass'])
        preparation = Preparation.objects.get(pk=request.data['preparation'])
        cocktail.ice = ice
        cocktail.glass = glass
        cocktail.preparation = preparation
        cocktail.save()
        serializer = CocktailSerializer(cocktail, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        ingredients = request.data.get('ingredients')
        CocktailIngredient.objects.filter(cocktail=cocktail).delete()
        for ingredient_object in ingredients:
            unit = Unit.objects.get(pk=ingredient_object['unit'])
            ingredient = Ingredient.objects.get(pk=ingredient_object['ingredient'])
            amount = float(ingredient_object['amount'])
            cocktail_ingredient = CocktailIngredient(unit=unit, ingredient=ingredient, amount=amount, cocktail=cocktail)
            cocktail_ingredient.save()
            
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        cocktail = Cocktail.objects.get(pk=pk)
        cocktail.delete()
        try:
            cocktail_ingredients = CocktailIngredient.objects.get(cocktail=pk)
            if cocktail_ingredients:
                for ingredient in cocktail_ingredients:
                    ingredient.delete()
        except:
            return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class CocktailSerializer(serializers.ModelSerializer):
    """JSON serializer for cocktails
    """
    ingredients = CocktailIngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Cocktail
        fields = ('id', 'name', 'description', 'instructions', 'img_url', 'creator', 'glass', 'ice', 'preparation', 'ingredients')
        depth = 2
        
class CreateCocktailSerializer(serializers.ModelSerializer):
    """JSON serializer for cocktails
    """
    ingredients = CocktailIngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Cocktail
        fields = ('id', 'name', 'description', 'instructions', 'img_url', 'glass', 'ice', 'preparation', 'ingredients')