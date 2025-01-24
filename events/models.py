from django.db import models
from users.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    attendees = models.ManyToManyField(User, related_name='attending_events')

    def __str__(self):
        return self.title
