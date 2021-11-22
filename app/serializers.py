from rest_framework import serializers
from .models import Dr


class DrSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dr
        fields = ['drid', 'prsnid', 'proid', 'uniid']