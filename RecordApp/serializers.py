from rest_framework import serializers
from RecordApp.models import eRecord

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = eRecord
        fields = "__all__"