from rest_framework import serializers
from .models import Empl_Details
from django.db.models import fields

class Empl_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empl_Details
        fields = '__all__'