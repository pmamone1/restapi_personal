from .models import Personal
from rest_framework import viewsets, permissions
from .serializers import PersonalSerializer

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    permission_classes = [permissions.AllowAny] # cualquier cliente puede pedir datos
    serializer_class = PersonalSerializer
    
    