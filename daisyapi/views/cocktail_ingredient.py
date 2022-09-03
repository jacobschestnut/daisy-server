"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daisyapi.models import CocktailIngredient


class CocktailIngredientView(ViewSet):
    """Daisy cocktail ingredient view"""

    def list(self, request):
        """Handle GET requests to get all cocktail ingredients for a cocktail

        Returns:
            Response -- JSON serialized list of cocktails
        """
        
        ingredients = CocktailIngredient.objects.all().order_by('-amount')
        cocktail = request.query_params.get('cocktail', None)
        if cocktail is not None:
            ingredients = ingredients.filter(cocktail=cocktail)
        serializer = CocktailIngredientSerializer(ingredients, many=True, context={'request':request})
        return Response(serializer.data)
    
    
class CocktailIngredientSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = CocktailIngredient
        fields = ('id', 'cocktail', 'amount', 'ingredient', 'unit')
        depth = 2