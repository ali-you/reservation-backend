from django.shortcuts import render
from rest_framework import generics
from .models import Dr
from .serializers import DrSerializer


class DrList(generics.ListAPIView):
    queryset = Dr.objects.all()
    serializer_class = DrSerializer
