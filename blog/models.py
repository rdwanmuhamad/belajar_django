from django.db import models

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=255, null=True)
    waktuPosting = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "{}. {}".format(self.id,self.title)