from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from Uid import genUid

from RecordApp.models import eRecord
from RecordApp.serializers import RecordSerializer
# Create your views here.

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def getRecords(request):
    records = eRecord.objects.all()
    recordSerializer = RecordSerializer(records, many=True)
    return Response(recordSerializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def addRecord(request):
    data = request.data
    data['id'] = genUid()
    recordSerializer = RecordSerializer(data=data)
    if recordSerializer.is_valid():
        recordSerializer.save()
        return Response(recordSerializer.data, status=status.HTTP_201_CREATED)
    return Response(recordSerializer.errors, status=status.HTTP_400_BAD_REQUEST)