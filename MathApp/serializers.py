from rest_framework import serializers
from MathApp.models import eMath

class MathSerializer(serializers.ModelSerializer):
    class Meta:
        model = eMath
        fields = "__all__"