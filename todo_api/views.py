from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from todo_api.serializer import TodoSerializer

from todo_api.models import TodoList

# Create your views here.

@api_view(['GET'])
def get_todo_data(request):
    todos = TodoList.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_todo_data(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def todos_all(request, pk):
    try:
        todo = TodoList.objects.get(pk=pk)
    except:
        return Response({'error':'Todo note exists'},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        todo.delete()
        return Response({'Deleted': 'success'})