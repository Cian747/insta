from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User,related_name='following', blank=True)
    bio = models.TextField(default="Hi I'm new here")
    profile_photo = models.ImageField(upload_to='images/',default= 'https://avataaars.io/?avatarStyle=Circle&topType=WinterHat3&accessoriesType=Round&hatColor=Gray02&facialHairType=MoustacheMagnum&facialHairColor=Red&clotheType=BlazerShirt&eyeType=Wink&eyebrowType=Angry&mouthType=Twinkle&skinColor=Black')
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def image_posts(self):
        return self.image_set.all()

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('profile',args=str([self.id]))

    @classmethod
    def search_by_user(cls,search_term):
        return cls.objects.filter(user__username__icontains = search_term)