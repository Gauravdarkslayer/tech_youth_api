from rest_framework import serializers
from .models import *


    #def __str__(self):
    #    return f"{instance.emailid}"

class interestSerializer(serializers.ModelSerializer):

    class Meta:
        model=interest
        fields='__all__'
        # fields = [
        #         'id',
        #         'question',
        #         ]
        # read_only_fields = ('question',)
        # depth=2

    def update(self, validated_data):
        instance = user.objects.get(emailid=validated_data.get('emailid'))
        # print(instance)
        # instance.usernamec  = validated_data.get('username')
        instance.interest = validated_data.get('interest')

        instance.save()
        return instance


class questionsSerializer(serializers.ModelSerializer):

    class Meta:
        model=questions
        fields='__all__'

    def update(self, validated_data):
        iid = user.objects.get(iid=validated_data.get('iid'))
        # print(instance)
        instance.question = validated_data.get('question')
        # instance.password = validated_data.get('password')

        instance.save()
        return instance


class userSerializer(serializers.ModelSerializer):
    # inte = interestSerializer(many=True,read_only=True)
    class Meta:
        model=user


        fields='__all__'



    def update(self, validated_data):
        instance = user.objects.get(emailid=validated_data.get('emailid'))
        # print(instance)
        instance.username = validated_data.get('username')
        instance.password = validated_data.get('password')

        instance.save()
        return instance


class allSerializer(serializers.ModelSerializer):
    # us = userSerializer(many=True)
    # inter = interestSerializer(many=True)
    # ques = questionsSerializer(many=True)

    class Meta:
        model=user,interest
        fields =[{user:['username','password','emailid'],
                    interest:['__all__']}]
