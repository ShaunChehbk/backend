from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from Uid import genUid
import random

from LinguistApp.models import (
    Word, RateHistory
)
from LinguistApp.serializers import (
    WordSerializer, RateHistorySerializer
)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def rate_word(request):
    data = request.data
    data['id'] = genUid()
    rate_history_serializer = RateHistorySerializer(data=data)
    if rate_history_serializer.is_valid():
        rate_history_serializer.save()
        return Response(rate_history_serializer.data, status=status.HTTP_201_CREATED)
    return Response(rate_history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def get_ten_words(request):
    words = Word.objects.all()
    result = random.sample(list(words), 10)
    words_serializer = WordSerializer(result, many=True)
    return Response(words_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated,))
def get_rate_history(request):
    rate_history = RateHistory.objects.all()
    response = []
    for h in rate_history:
        word = Word.objects.filter(id=h.word)[0]
        response.append({
            "id": h.id,
            "content": word.content, 
            "rate": h.rate
        })
    return Response(response, status=status.HTTP_200_OK)