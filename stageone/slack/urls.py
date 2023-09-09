"""
A module that defines the endpoints
"""
from django.urls import path
from slack.views import Details

urlpatterns = [
        path('api/', Details.as_view()),
]
