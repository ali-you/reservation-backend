from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Dr, Hosp, Patient, Person, Pharmacy, Proficiency, Uni, Visit, Work
from .serializers import *


class DrList(generics.ListCreateAPIView):
    queryset = Dr.objects.all()
    serializer_class = DrSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HospList(generics.ListCreateAPIView):
    queryset = Hosp.objects.all()
    serializer_class = HospSerializer


class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PharmacyList(generics.ListCreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer


class ProficiencyList(generics.ListCreateAPIView):
    queryset = Proficiency.objects.all()
    serializer_class = ProficiencySerializer


class UniList(generics.ListCreateAPIView):
    queryset = Uni.objects.all()
    serializer_class = UniSerializer


class VisitList(generics.ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class WorkList(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
