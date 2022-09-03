"""View module for handling requests about cocktails"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from daisyapi.models import Cocktail


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
    
    
class CocktailSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Cocktail
        fields = ('id', 'name', 'description', 'instructions', 'img_url', 'creator', 'glass', 'ice', 'preparation')
        depth = 1