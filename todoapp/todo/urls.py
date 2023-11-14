from django.urls import path
from .views import createTodo

urlpatterns = [
    path('createTodo/',createTodo,name='createtodo'),
]