
from django.db import models

class Article(models.Model):
    author = models.CharField(max_length = 120)
    title = models.CharField(max_length = 120)
    text = models.TextField()
    password = models.CharField(max_length = 120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} / {}".format(self.author,self.title) 