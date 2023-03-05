from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from Uid import genUid

from TodoApp.models import eTodo
from TodoApp.serializers import TodoSerializer

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def getTodos(request):
    records = eTodo.objects.all()
    todoSerializer = TodoSerializer(records, many=True)
    return Response(todoSerializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def addTodo(request):
    data = request.data
    data['id'] = genUid()
    todoSerializer = TodoSerializer(data=data)
    if todoSerializer.is_valid():
        todoSerializer.save()
        return Response(todoSerializer.data, status=status.HTTP_201_CREATED)
    return Response(todoSerializer.errors, status=status.HTTP_400_BAD_REQUEST)