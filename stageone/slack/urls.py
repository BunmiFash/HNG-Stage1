"""
ENDPOINTS FOR SLACK APP
"""
from django.urls import path
from slack import views

urlpatterns = [
        path('details/', views.ListDetails.as_view()),
]
