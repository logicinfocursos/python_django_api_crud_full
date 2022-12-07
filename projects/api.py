from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjecViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny] #cors
    serializer_class = ProjectSerializer