"""
A module that serializes objects
"""
from rest_framework import serializers
from .models import SlackDetails


class SlackDetailsSerializer(serializers.ModelSerializer):
    """
    Serializes SlackDetails objects
    """
    class Meta:
        model = SlackDetails
        fields = '__all__'
