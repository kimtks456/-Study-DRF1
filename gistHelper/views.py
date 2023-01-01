from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from gistHelper.models import Mealplan
from gistHelper.serializer import Serializer


# Create your views here.

class MealplanList(APIView):
    def get(self, request):
        meals = Mealplan.objects.all()
        serializer = Serializer(meals, many=True)
        return Response(serializer.data)

    def post(selfself, request):
        serializer = Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

