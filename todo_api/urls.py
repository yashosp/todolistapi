from django.contrib import admin
from django.urls import path

from todo_api.views import get_todo_data, post_todo_data, todos_all

urlpatterns = [
    path('',get_todo_data),
    path('todo_post', post_todo_data),
    path('<int:pk>/', todos_all)
]
