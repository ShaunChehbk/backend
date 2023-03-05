from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from MathApp.models import eMath
from MathApp.serializers import MathSerializer

from Uid import genUid

# Create your views here.

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def getMathNotes(request):
    mathNotes = eMath.objects.all()
    mathNotesSerializer = MathSerializer(mathNotes, many=True)
    return Response(mathNotesSerializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addMathNote(request):
    data = request.data
    data['id'] = genUid()
    mathSerializer = MathSerializer(data=data)
    if mathSerializer.is_valid():
        mathSerializer.save()
        return Response(mathSerializer.data, status=status.HTTP_201_CREATED)
    return Response(mathSerializer.errors, status=status.HTTP_400_BAD_REQUEST)