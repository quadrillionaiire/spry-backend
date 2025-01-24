from django.contrib.auth.models import AbstractUser
from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):  # Inherits from Django's default user model
    email = models.EmailField(unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    class_year = models.IntegerField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')
    bio = models.TextField(null=True, blank=True)  # Add a bio field
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Profile pic field
    social_links = models.JSONField(null=True, blank=True)  # Dictionary for social media links (e.g., {'twitter': '', 'linkedin': ''})
    friends = models.ManyToManyField('self', blank=True)  # Friends list (mutual relationship)


    # Specify related_name to avoid conflict with the built-in User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Use a unique related name to avoid clash
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Unique related name
        blank=True,
    )

    def __str__(self):
        return self.username

class ClassCode(models.Model):
    code = models.CharField(max_length=8, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_year = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
