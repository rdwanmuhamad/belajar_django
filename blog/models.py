from django.db import models

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
<<<<<<< HEAD
    category = models.CharField(max_length=255, null=True)
    waktuPosting = models.DateTimeField(auto_now_add=True, null=True)
=======
    email = models.EmailField(default='nama@email.test')
    alamat = models.CharField(max_length=255, blank=True,)
    
>>>>>>> 87d345168b4f22226a273ec980f023f4d6a27cf8

    def __str__(self):
        return "{}. {}".format(self.id,self.title)