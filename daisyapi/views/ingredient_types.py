"""View module for handling requests about ingredient types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from daisyapi.models.ingredient_type import IngredientType

class IngredientTypeView(ViewSet):
    """Daisy ingredient types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single ingredient type

        Returns:
            Response -- JSON serialized cocktail
        """
        
        try:
            ingredient_type = IngredientType.objects.get(pk=pk)
            serializer = IngredientTypeSerializer(ingredient_type)
            return Response(serializer.data)
        except IngredientType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
    

    def list(self, request):
        """Handle GET requests to get all ingredient types

        Returns:
            Response -- JSON serialized list of ingredient types
        """
        
        ingredient_types = IngredientType.objects.all()
        serializer = IngredientTypeSerializer(ingredient_types, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized ingredient type instance
        """
        serializer = IngredientTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ingredient_type = serializer.save()
        res_serializer = IngredientTypeSerializer(ingredient_type)
        return Response(res_serializer.data, status=status.HTTP_201_CREATED)
    
class IngredientTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for ingredient types
    """
    class Meta:
        model = IngredientType
        fields = ('id', 'label')