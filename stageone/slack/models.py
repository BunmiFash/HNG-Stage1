from django.db import models
from django.utils import timezone
from datetime import datetime

"""
A module that defines all the attribute
the slack objects
"""


class SlackDetails(models.Model):
    """
    class attirbutes
    """
    slack_name = models.CharField(max_length=100, null=False)
    current_day = models.DateField(blank=True, null=True)
    utc_time = models.DateTimeField( blank=True, null=True)
    track = models.CharField(max_length=100, null=False)
    github_file_url = models.CharField(max_length=100, null=False)
    github_repo_url = models.CharField(max_length=100, null=False)
    status_code = models.IntegerField(null=True)

    def __str__(self):
        """
        String representation of objects
        """
        return self.slack_name
