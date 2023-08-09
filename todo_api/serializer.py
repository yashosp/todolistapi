from rest_framework import serializers
from todo_api.models import TodoList

# class TodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TodoList
#         fields = '__all__'
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'