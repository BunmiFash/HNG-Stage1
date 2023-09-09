"""
A module that converts objects
into json formats
"""
from rest_framework import serializers
from slack.models import SlackDetails


class SlackDetailsSerializer(serializers.ModelSerializer):
    """
    converts python object to json
    """
    class Meta:
        model = SlackDetails
        fields = ["slack_name", "current_day", "utc_time",  "track", "github_file_url", "github_repo_url", "status_code"]
