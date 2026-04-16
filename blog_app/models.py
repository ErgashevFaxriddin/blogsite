from django.db import models
from django.contrib.auth.models import User #user uchun models tayyor, userga xususiyatlar qoshamiz
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publishied', 'Published')
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date="publish") #sana boyicha unique qiladi
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()


posts = Post.objects.filter(status='published')
p_posts = Post.published.all()