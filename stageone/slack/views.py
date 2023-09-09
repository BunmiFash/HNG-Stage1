"""
ALL requests
"""
from django.shortcuts import render
from slack.serializers import SlackDetailsSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from slack.models import SlackDetails
from django.http import HttpResponse
import datetime


class Details(generics.ListAPIView):
    serializer_class = SlackDetailsSerializer

    def get_queryset(self):
        qs = SlackDetails.objects.all()
        return qs

    def get(self, request, *args, **kwargs):
        try:
            name = self.request.query_params['slack_name']
            track = self.request.query_params['track']

            if track is not None and name is not None:
                qs = SlackDetails.objects.get(slack_name=name, track=track)
                qs.status_code = HttpResponse.status_code
                qs.save()
                serializer = SlackDetailsSerializer(qs)
        except Exception as e:
            print(e)
            qs = self.get_queryset()
            for obj in qs:
                p = obj.__dict__
                p['status_code'] = HttpResponse.status_code
            serializer = SlackDetailsSerializer(qs, many=True)

        return Response(serializer.data)
