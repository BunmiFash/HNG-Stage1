"""
Endpoints
"""

from django.shortcuts import render
from .models import SlackDetails
from .serializers import SlackDetailsSerializer
from rest_framework import generics
from rest_framework.views import APIView


class ListDetails(generics.ListAPIView):
    queryset = SlackDetails.objects.all()
    serializer_class = SlackDetailsSerializer
    
    def get_query(self):
        queryset = SlackDetails.objects.all()
        name = self.requests.get_param.get('slack_name')
        track = self.requests.get_param.get('track')i
        print(queryset)

