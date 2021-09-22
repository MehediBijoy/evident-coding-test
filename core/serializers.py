from django.db.models import fields
from rest_framework import serializers
from .models import searchModel

# model serializer convert model object to json data
class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = searchModel
        fields = ['id', 'input_value', 'timestamp']