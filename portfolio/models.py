from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phn_num = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Blogs(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to="blog", blank=True, null=True)
    auth_name = models.CharField(max_length=50)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title