from django.db import models

# Create your models here.

class Song(models.Model):
    song_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 150, null=False, blank = False)
    image = models.ImageField(upload_to = 'image')
    audio = models.FileField(upload_to= 'audio')
    duration= models.IntegerField( blank = False)
    time= models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        return self.name
    