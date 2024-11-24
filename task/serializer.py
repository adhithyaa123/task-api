from task.models import Task

from rest_framework import serializers

from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):

    class Meta:

        model=Task

        fields="__all__"

        read_only_fields=["owner","created_date",]

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["username","password","email"]

    def create(self,validated_data):
        
        return User.objects.create_user(**validated_data)    


