"""View module for handling requests about ice"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from daisyapi.models import Ice

class IceView(ViewSet):
    """Daisy ice view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single ice

        Returns:
            Response -- JSON serialized ice
        """
        
        try:
            ice = Ice.objects.get(pk=pk)
            serializer = IceSerializer(ice)
            return Response(serializer.data)
        except Ice.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
    

    def list(self, request):
        """Handle GET requests to get all ices

        Returns:
            Response -- JSON serialized list of ices
        """
        
        ice = Ice.objects.all()
        serializer = IceSerializer(ice, many=True)
        return Response(serializer.data)
    
class IceSerializer(serializers.ModelSerializer):
    """JSON serializer for ices
    """
    class Meta:
        model = Ice
        fields = ('id', 'label')      