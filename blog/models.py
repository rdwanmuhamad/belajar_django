from django.db import models

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    email = models.EmailField(default='nama@email.test')
    alamat = models.CharField(max_length=255, blank=True,)
    

    def __str__(self):
        return "{}. {}".format(self.id,self.title)