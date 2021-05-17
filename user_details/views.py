from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import Users

# Create your views here.


# ********** seperate api's  ***************
@csrf_exempt
@api_view(["GET"])
def all_users(request):
        user = Users.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)
@csrf_exempt
@api_view(["POST"])
def add_user(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
@api_view(["GET"])
def get_user(request,pk):
    user = validate_user(pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@csrf_exempt
@api_view(["PUT"])
def modify_user(request, pk):
    user = validate_user(pk)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["DELETE"])
def delete_user(request, pk):
    user = validate_user(pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

def validate_user(pk):
    try:
        user = Users.objects.get(pk=pk)
        return user
    except Users.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


