from django.db import models
from django.contrib.auth.models import User
from .book import Book

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)