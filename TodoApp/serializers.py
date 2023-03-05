from rest_framework import serializers
from TodoApp.models import eTodo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = eTodo
        fields = "__all__"