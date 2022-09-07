"""View module for handling requests about preparations"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from daisyapi.models import Preparation

class PreparationView(ViewSet):
    """Daisy preparation view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single preparation

        Returns:
            Response -- JSON serialized preparation
        """
        
        try:
            preparation = Preparation.objects.get(pk=pk)
            serializer = PreparationSerializer(preparation)
            return Response(serializer.data)
        except Preparation.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
    

    def list(self, request):
        """Handle GET requests to get all preparations

        Returns:
            Response -- JSON serialized list of preparations
        """
        
        preparations = Preparation.objects.all()
        serializer = PreparationSerializer(preparations, many=True)
        return Response(serializer.data)
    
class PreparationSerializer(serializers.ModelSerializer):
    """JSON serializer for preparations
    """
    class Meta:
        model = Preparation
        fields = ('id', 'label')      