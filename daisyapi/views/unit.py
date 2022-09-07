"""View module for handling requests about units"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from daisyapi.models import Unit

class UnitView(ViewSet):
    """Daisy unit view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single unit

        Returns:
            Response -- JSON serialized unit
        """
        
        try:
            unit = Unit.objects.get(pk=pk)
            serializer = UnitSerializer(unit)
            return Response(serializer.data)
        except Unit.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 
    

    def list(self, request):
        """Handle GET requests to get all units

        Returns:
            Response -- JSON serialized list of units
        """
        
        unit = Unit.objects.all()
        serializer = UnitSerializer(unit, many=True)
        return Response(serializer.data)
    
class UnitSerializer(serializers.ModelSerializer):
    """JSON serializer for glass
    """
    class Meta:
        model = Unit
        fields = ('id', 'label')      