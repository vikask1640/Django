from django.db import models
import datetime
class Post(models.Model):
    title=models.CharField(max_length=140)
    body=models.TextField()
    date=models.DateTimeField('date published')

    def __str__(self):
        return self.title
