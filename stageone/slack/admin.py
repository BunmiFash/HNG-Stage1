"""
A module that registers the class as
a table in the database
"""
from django.contrib import admin
from slack.models import SlackDetails

admin.site.register(SlackDetails)
