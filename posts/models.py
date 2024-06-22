from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    

class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.SET_NULL, blank=True, null=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)