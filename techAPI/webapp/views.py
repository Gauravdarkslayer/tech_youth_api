# from django.shortcuts import render
from django.http import Http404
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
            # return Response({"Successfully Added User : ",f"{user_saved}")
            return Response({"success":f"User {user_saved}added successfully"})

   

    def put(self,request,format=None):   #pk --> Primary key

        #user=self.get_object(pk)
        #print(user)
        serializer=userSerializer()
        serializer.update(validated_data=request.data)
        return Response("Success")
        # return Response({"success": "User '{}' updated successfully".format(dataa)})


    def delete(self,request,pk):
         # Get object with this pk
        to_delete_user= get_object_or_404(user.objects.all(), pk=pk)
        to_delete_user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)},status=204)


class interestList(APIView):

    def get(self,request):
        interest1=interest.objects.all()
        serializer=interestSerializer(interest1,many=True)
        return Response(serializer.data)

    def post(self,request):
       serializer=interestSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
           interest_saved=serializer.save()
       return Response("Successfully Added Interest : ",interest_saved," for User")

    def put(self,request,format=None):   #pk --> Primary key

        #user=self.get_object(pk)
        #print(user)
        serializer=userSerializer()
        serializer.update(validated_data=request.data)
        return Response("Success")
        # return Response({"success": "Interest '{}' updated successfully".format(dataa)})

    def delete(self,request,pk):
         # Get object with this pk
        to_interest_delete = get_object_or_404(user.objects.all(), pk=pk)
        to_interest_delete.delete()
        return Response({"message": "Interest with id `{}` has been deleted.".format(pk)},status=204)

class questionsList(APIView):

    def get(self,request):
        question=questions.objects.all()
        serializer=questionsSerializer(question,many=True)
        return Response(serializer.data)

    def post(self,request):
        # question=request.data.get('question')
        serializer=questionsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            question_save=serializer.save()
        return Response({"success":f"Successfully Added # QUESTION:  : {question_save} for User"})

    def put(self):
       pass

    def delete(self,request,pk):
         # Get object with this pk
        to_question_delete = get_object_or_404(user.objects.all(), pk=pk)
        to_question_delete.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)
