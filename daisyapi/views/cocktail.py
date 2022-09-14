"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daisyapi.models import Cocktail
from daisyapi.models.mixologist import Mixologist
from daisyapi.models.ingredient import Ingredient
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
        
        cocktails = Cocktail.objects.all()
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
                ing_obj = Ingredient.objects.get(pk=data_ingredient['ingredient'])
                cocktail_serializer = CocktailIngredientSerializer(data=data_ingredient)
                cocktail_serializer.is_valid(raise_exception=True)
                cocktail_ingredient = cocktail_serializer.save(cocktail=new_cocktail,ingredient=ing_obj)
                cocktail_res_serializer = CocktailIngredientSerializer(cocktail_ingredient)
        return Response(res_serializer.data, status=status.HTTP_201_CREATED)
    
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