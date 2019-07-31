from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *
# Create your views here.

class userList(APIView):

    def get(self,request):
        username1=user.objects.all()
        serializer=userSerializer(username1,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=userSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_saved=serializer.save()
            print(user_saved)
            return Response("Successfully Added User : ",f"{user_saved}")

    def put(self,request,pk):
        saved_article = get_object_or_404(user.objects.all(),pk=pk)
        # data = request.data.get('article')
        dataa = userSerializer()
        dataa.update(instance=saved_article, validated_data=request.data)
        # serializer = userSerializer(instance=saved_article, data=request.data, partial=True)
        if dataa.is_valid(raise_exception=True):
            article_saved = dataa.save()
        return Response({"success": "User '{}' updated successfully".format(article_saved)})


    def delete(self,request,pk):
         # Get object with this pk
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)


class interestList(APIView):

    def get(self,request):
        interest1=interest.objects.all()
        serializer=interestSerializer(interest1,many=True)
        return Response(serializer.data)
    def post(self,request):

       serializer=interestSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
           interest_saved=serializer.save()
       return Response("Successfully Added Interest : ",interest_saved.title," for User")

    def put(self):
        pass

    def delete(self):
        pass
class questionsList(APIView):

    def get(self,request):
        question=questions.objects.all()
        serializer=questionsSerializer(question,many=True)
        return Response(serializer.data)
    def post(self,request):
        # question=request.data.get('question')
        serializer=questionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            question_save=serializer.save()
        return Response("Successfully Added Interest : ",question_save.title," for User")
    def put(self):
       pass

    def delete(self):
        pass
