# core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Project, ProjectAPIKey
from .permissions import IsEditor

class GenerateAPIKeyView(APIView):
    def post(self, request):
        project, _ = Project.objects.get_or_create(name="DemoProject")
        api_key, key = ProjectAPIKey.objects.create_key(name="DemoKey", project=project)
        return Response({"api_key": key})

class EditorOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsEditor]

    def get(self, request):
        return Response({"message": "Welcome, Editor!"})