from django.db import models
from django.contrib.auth.models import User #user uchun models tayyor, userga xususiyatlar qoshamiz
from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date="publish") #sana boyicha unique qiladi
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)