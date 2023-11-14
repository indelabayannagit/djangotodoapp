from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def createTodo(request):
    data = request.data
    print(data)
    return JsonResponse(data,safe=False)