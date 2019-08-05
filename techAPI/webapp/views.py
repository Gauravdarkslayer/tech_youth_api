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
        # inte = interest.objects.all()
        # # question=questions.objects.all()
        serializer=userSerializer(username1,many=True)

        # for i in range(len(dataa1)):
        #     for j in range(len(dataa)):
        #         if dataa[0]['emailid']==dataa1[0]['emailid']:
        #         dict1={'id':dataa1[0]['id'],'interest':dataa1[0]['interest']}
        #         dataa.extend([(dict1)])
        #         print(dataa)
        #         return Response(dataa)
        # return Response({"fail":"not validated_data"})
        return Response(serializer.data)

    def get(self,request,var):
        username1=user.objects.get(emailid=var)
        current_user=userSerializer(username1,many=True)
        return Response(current_user.data)


    def post(self,request):
        serializer=userSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_saved=serializer.save()
# <<<<<<< HEAD
            # return Response({"success":f"User {user_saved}added successfully"})
            return Response(serializer.data)
        return Response("Failed To Post Data")
# =======
#             return Response({"success":f"User {user_saved}added successfully"})
#             return Response({serializer.data})

# >>>>>>> b8e3a5f3ee6a265dbb30966d7e5a81dda47c1e16


    def put(self,request,format=None):   #pk --> Primary key
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
       return Response({"success":f"Successfully Added Interest : {interest_saved}, for User"})

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

    def put(self,request,format=None):   #pk --> Primary key
        serializer=userSerializer()
        serializer.update(validated_data=request.data)
        return Response("Success")
        # return Response({"success": "Interest '{}' updated successfully".format(dataa)})


    def delete(self,request,pk):
         # Get object with this pk
        to_question_delete = get_object_or_404(user.objects.all(), pk=pk)
        to_question_delete.delete()
        return Response({"message": "# QUESTION:  with id `{}` has been deleted.".format(pk)},status=204)


@api_view('GET')
def user(var):
