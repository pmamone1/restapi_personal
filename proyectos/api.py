from .models import Proyectos
from rest_framework import viewsets, permissions
from .serializers import ProyectoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyectos.objects.all()
    permission_classes = [permissions.AllowAny] # cualquier cliente puede pedir datos
    serializer_class = ProyectoSerializer
    
    