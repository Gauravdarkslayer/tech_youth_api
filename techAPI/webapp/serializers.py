from rest_framework import serializers
from .models import *

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model=user
        fields='__all__'


    def update(self, instance, validated_data):
        instance.emailid = validated_data.get('emailid', instance.emailid)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        # instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance

class interestSerializer(serializers.ModelSerializer):

    class Meta:
        model=interest
        fields='__all__'

class questionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=questions
        fields='__all__'
