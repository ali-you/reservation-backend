from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Dr
from .serializers import DrSerializer


class DrList(generics.ListCreateAPIView):
    queryset = Dr.objects.all()
    serializer_class = DrSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
