"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daisyapi.models import Cocktail
from daisyapi.models import Glass, Ice, Preparation
from daisyapi.models.cocktail_ingredient import CocktailIngredient
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
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized cocktail instance
        """
        creator = Mixologist.objects.get(user=request.auth.user)
        ingredients = request.data.get("ingredients")
        if ingredients:
            del request.data["ingredients"]
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
        # creator = Mixologist.objects.get(pk=request.data["creator"])
        ice = Ice.objects.get(pk=request.data['ice'])
        glass = Glass.objects.get(pk=request.data['glass'])
        preparation = Preparation.objects.get(pk=request.data['preparation'])
        # ingredients = request.data.get("ingredients")
        # if ingredients:
        #     del request.data["ingredients"]
        # cocktail.creator = creator
        cocktail.name = request.data["name"]
        cocktail.description = request.data["description"]
        cocktail.instructions = request.data["instructions"]
        cocktail.img_url = request.data["img_url"]
        cocktail.glass = glass
        cocktail.ice = ice
        cocktail.preparation = preparation
        # if ingredients:
        #     for cock_ing in ingredients:
        #         print(cock_ing)
        #         ing_obj = Ingredient.objects.get(pk=cock_ing['ingredient'])
        #         cocktail = Cocktail.objects.get(pk=pk)
        #         unit = Unit.objects.get(pk=cock_ing['unit'])
        #         cock_ing["ingredient"] = ing_obj
        #         cock_ing['cocktail'] = cocktail
        #         cock_ing['unit'] = unit
        #         cock_ing['amount'] = cock_ing['amount']
        #         cock_ing.save()
        #         ing_obj = CocktailIngredient.objects.get(pk=data_ingredient['ingredient'])
        #         cocktail_serializer = CocktailIngredientSerializer(data=data_ingredient)
        #         cocktail_serializer.is_valid(raise_exception=True)
        #         cocktail_ingredient = cocktail_serializer.save(cocktail=cocktail,ingredient=ing_obj)
        #         cocktail_res_serializer = CocktailIngredientSerializer(cocktail_ingredient)
        # ingredients = CocktailIngredient.objects.get(pk=request.data["cocktail_ingredient"])
        # cocktail.ingredients = ingredients
        print(cocktail)
        cocktail.save()

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
    """JSON serializer for game types
    """
    class Meta:
        model = Cocktail
        fields = ('id', 'name', 'description', 'instructions', 'img_url', 'creator', 'glass', 'ice', 'preparation')
        depth = 2
        
class CreateCocktailSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Cocktail
        fields = ('id', 'name', 'description', 'instructions', 'img_url', 'glass', 'ice', 'preparation')