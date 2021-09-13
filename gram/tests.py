from django.test import TestCase
from .models import Image,Comment
from django.contrib.auth.models import User
from profiles.models import Profile

# Create your tests here.

class TestInstaClass(TestCase):

    def setUp(self):
        '''
        Set up the classes
        '''
        self.new_user = User(id = 1,first_name = 'James', last_name ='Muriuki', username = 'james12',email ='james@moringaschool.com')
        self.new_user.save()

        self.new_profile = Profile(id = 10, user = self.new_user, bio = 'New here',profile_photo='image.jpg',updated ='1901-08-09' ,created_at = '1900-08-09')

        self.new_images = Image(id = 1,image = 'tall.jpg',image_name = 'Junior', image_caption = 'posted',profile = self.new_profile, created = '1999-09-08',updated = '2000-09-08')
        self.new_images.save()

        self.comment = Comment(comment = 'Hello World',user_id = self.new_user,image = self.new_images)
        self.comment.save()

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()
        Comment.objects.all().delete()

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_image_instance(self):
        self.assertTrue(isinstance(self.new_images,Image))

    def test_comment_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_save_image(self):
        self.new_images.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==1)

    def test_save_comment(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)==1)

    # def test_save_profile(self):
    #     self.new_profile.save_profile()
    #     profile = Profile.objects.all()
    #     self.assertTrue(len(profile)==1)

    def test_delete_image(self):
        self.new_images.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test_delete_comment(self):
        self.comment.delete_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)==0)

    # def test_delete_profile(self):
    #     self.new_profile.save_profile()
    #     self.new_profile.delete_profile()
    #     profiles = Profile.objects.all()
    #     self.assertTrue(len(profiles)==0)


    def test_update_images(self):
        '''
        Update image class
        '''
        self.new_images.save()
        image = Image.objects.last().id
        Image.update_image_caption(image,'the best')
        update_image = Image.objects.get(id = image)
        self.assertEqual(update_image.image_caption,'the best') 

    def test_update_profile(self):
        '''
        Update profile
        '''
        self.new_profile.save()
        profile = Profile.objects.last().id
        Profile.update_profile_bio(profile,'The man')
        update_profile = Profile.objects.get(id = profile)
        self.assertEqual(update_profile.bio,'The man')

    def test_search_by_user(self):
        '''
        test if you can search for a user
        '''
        users = Profile.search_by_user('james12')
        self.assertTrue(len(users)==1)



    