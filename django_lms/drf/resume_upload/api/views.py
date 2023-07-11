from django.shortcuts import render
from rest_framework.response import Response
from api.serializers import *
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.


class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Resume Uploaded Successfully', 
                             'status': 'success', 'canidate': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.error)
        
