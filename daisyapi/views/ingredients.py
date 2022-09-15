"""View module for handling requests about ingredients"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from daisyapi.models import Ingredient

class IngredientView(ViewSet):
    """Daisy ingredient view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single ingredient

        Returns:
            Response -- JSON serialized cocktail
        """
        
        try:
            ingredient = Ingredient.objects.get(pk=pk)
            serializer = IngredientSerializer(ingredient)
            return Response(serializer.data)
        except Ingredient.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
    

    def list(self, request):
        """Handle GET requests to get all ingredients

        Returns:
            Response -- JSON serialized list of ingredients
        """
        
        ingredients = Ingredient.objects.all().order_by('name')
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized ingredient instance
        """
        serializer = CreateIngredientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ingredient = serializer.save()
        res_serializer = CreateIngredientSerializer(ingredient)
        return Response(res_serializer.data, status=status.HTTP_201_CREATED)
    
class IngredientSerializer(serializers.ModelSerializer):
    """JSON serializer for ingredients
    """
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'type')
        depth = 2
        
class CreateIngredientSerializer(serializers.ModelSerializer):
    """JSON serializer for ingredients
    """
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'type')