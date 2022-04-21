from django.db import models

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=255)
    class meta:
        ...

class Comment(models.Model):
    comment = models.TextField()
    class meta:
        ...