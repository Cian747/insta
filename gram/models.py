from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from profiles.models import Profile

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=255)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='image_posts')

    def get_absolute_url(self):
        return reverse('image_detail',args=[str(self.image.id)])


    def total_likes(self):
        return self.likes.count()

    def save_image(self):
        self.save() 

    def __str__(self):
        return str(self.image_name)

    def delete_image(self):
        self.delete()


    @classmethod
    def update_image_caption(cls, id,image_caption):
        return cls.objects.filter(id = id).update(image_caption=image_caption)


    class Meta:
        ordering = ['-created',]


    
class Comment(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)


    def __str__(self):
        return self.comment

    def save_comment(self):
        return self.save()

    def delete_comment(self):
        self.delete()





    

