from django.db import models
from users.models import User

class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100, null=True, blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_postings')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

