from ast import For
import re
from urllib import response
from django.shortcuts import render, redirect
from yaml import serialize
from .serializers import UserRegister,UserDataSerializer #Serializer classs for Validation
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.parsers import JSONParser
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_swagger import renderers
from rest_framework.permissions import AllowAny
# Create your views here.
from rest_framework.schemas import AutoSchema
# import coreapi
# from coreapi.document import Field
from rest_framework.schemas import coreapi
from rest_framework.decorators import schema



#Register New User
class RegisterUser(APIView):
    
    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='New User Registered'
            data['username']=account.username
            data['phone']=account.phone
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)


#welcome window
class welcome(APIView):
    permission_classes =(IsAuthenticated,)
    
    def get(self,request):
        content={'user':str(request.user),'userid':str(request.user.id)}
        return Response(content)



#User Details Edit,Update,Delete Function
class userDetails(APIView):
    def get_object(self,pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self,request,pk,format=None):
        userData=self.get_object(pk)
        serializer=UserDataSerializer(userData)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        userData=self.get_object(pk)
        serializer=UserDataSerializer(userData,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message':'error','error':serializer.errors})
    def delete(self,request,pk,format=None):
        userData=self.get_object(pk)
        userData.delete()
        return Response({'message':"user deleted"})



class setPagination(PageNumberPagination):
    page_size=4



class paginationApi(ListAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserDataSerializer
    pagination_class=setPagination
    filter_backends=(SearchFilter,)
    search_fields=('username','phone','first_name','last_name')



    