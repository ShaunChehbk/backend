from rest_framework import serializers
from LinguistApp.models import (
    Word, RateHistory
)

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"

class RateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RateHistory
        fields = "__all__"