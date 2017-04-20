from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Board(models.Model):
    CATEGORY_CHOICES = (
        ('1','스트레칭'),('2','유산소운동'),('3','근력운동'),
    )
    CATEGORY_DICT = {label:value for (value, label) in CATEGORY_CHOICES}

    title = models.CharField(max_length = 50, unique = True)
    slug=models.SlugField(allow_unicode=True)
    photo = models.ImageField(blank= True)
    category = models.CharField(max_length=1,
        choices=CATEGORY_CHOICES,
        default = '5')
    instruction = models.TextField()
    outcomes = models.TextField()
    links = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    board = models.ForeignKey(Board)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.message

class Food(models.Model):
    title = models.CharField(max_length = 50, unique = True)
    slug=models.SlugField(allow_unicode=True)
    photo = models.ImageField(blank= True)
    instruction = models.TextField()
    direction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.title