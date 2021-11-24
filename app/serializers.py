from rest_framework import serializers
from .models import Dr, Work, Visit, Uni, Proficiency, Person, Hosp, Patient, Pharmacy


class DrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dr
        fields = ['drid', 'prsnid', 'proid', 'uniid']


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['workid', 'hospid', 'fee', 'start', 'end', 'weekday', 'drid']


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['visitid', 'visitdate', 'appointmentdate', 'status', 'drid', 'patientid']


class UniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uni
        fields = ['uniid', 'uniname']


class ProficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proficiency
        fields = ['proid', 'proname']


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['pharid', 'pharname', 'address', 'city', 'pharphone', 'zipcode', 'drid']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['prsnid', 'prsnname', 'lastname', 'prsnphone', 'address', 'city', 'gender', 'birth']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['patientid', 'height', 'weight', 'prsnid', 'emergencycontact']


class HospSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hosp
        fields = ['hospid', 'hospname', 'address', 'city', 'hospnumber', 'zipcode']
