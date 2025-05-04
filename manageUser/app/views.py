# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsManager, IsResearcher
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import ToolUser
from .serializers import ToolUserSerializer

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"msg": "Hello Admin"})

class ManagerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request):
        return Response({"msg": "Hello Manager or Admin"})

class ResearcherOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsResearcher]

    def get(self, request):
        return Response({"msg": "Hello Researcher or higher"})




class CreateReadUser(ListCreateAPIView):
    queryset = ToolUser.objects.all()
    serializer_class = ToolUserSerializer
    def perform_create(self, serializer):
        """Override this method to customize the creation logic if needed."""
        serializer.save()


class UpdateDeleteViewUser(RetrieveUpdateDestroyAPIView):
    queryset = ToolUser.objects.all()  
    serializer_class = ToolUserSerializer
    