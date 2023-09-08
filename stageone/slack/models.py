from django.db import models
import datetime
from django.utils import timezone

# Create your models here

class SlackDetails(models.Model):
    slack_name = models.CharField(max_length=100)
    current_day = models.DateTimeField(default=datetime.datetime.now().day)
    utc_time = models.DateTimeField(default=timezone.now()) 
    track = models.CharField(max_length=100)
    github_file_url = models.CharField(max_length=100)
    github_repo_url = models.CharField(max_length=100)
    status_code =  models.IntegerField()
