from rest_framework import serializers
from .models import *

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model=user
        fields='__all__'


    def update(self, validated_data):
        instance = user.objects.get(emailid=validated_data.get('emailid'))
        print(instance)
        #instance.username =
        #instance.emailid = validated_data.get('emailid', instance.emailid)
        instance.username = validated_data.get('username')
        instance.password = validated_data.get('password')
        # instance.author_id = validated_data.get('author_id')

        instance.save()
        return instance

    #def __str__(self):
    #    return f"{instance.emailid}"

class interestSerializer(serializers.ModelSerializer):

    class Meta:
        model=interest
        fields='__all__'

    def update(self, instance, validated_data):
        instance.emailid = validated_data.get('emailid', instance.emailid)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)

class questionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=questions
        fields='__all__'

    def update(self, instance, validated_data):
        instance.emailid = validated_data.get('emailid', instance.emailid)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
