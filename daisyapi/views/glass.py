"""View module for handling requests about Glass"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from daisyapi.models import Glass

class GlassView(ViewSet):
    """Daisy Glass view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Glass

        Returns:
            Response -- JSON serialized Glass
        """
        
        try:
            glass = Glass.objects.get(pk=pk)
            serializer = GlassSerializer(glass)
            return Response(serializer.data)
        except Glass.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
    

    def list(self, request):
        """Handle GET requests to get all Glass

        Returns:
            Response -- JSON serialized list of Glass
        """
        
        glass = Glass.objects.all()
        serializer = GlassSerializer(glass, many=True)
        return Response(serializer.data)
    
class GlassSerializer(serializers.ModelSerializer):
    """JSON serializer for glass
    """
    class Meta:
        model = Glass
        fields = ('id', 'label')      