from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from .models import Task

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
# Create your views here.


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List': '/task_list/',
        'Detail': '/detail/<str:pk>',
        'Create': '/create/',
        'Update': '/update/<str:pk>',
        'Delete': '/delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def detailView(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializers(task, many = False)
    return Response(serializer.data)



@api_view(['POST'])
def createView(request):
    serializer = TaskSerializers(data = request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)



@api_view(['POST'])
def updateView(request, pk):
    task = Task.objects.get(id = pk)

    serializer = TaskSerializers(instance = task , data = request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteView(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Item successfully deleted!")
    