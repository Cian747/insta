# Generated by Django 3.2.7 on 2021-09-14 11:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=cloudinary.models.CloudinaryField(blank=True, default='/media/images/joni-rajala-1qJh1aORn_Q-unsplash.jpg', max_length=255, null=True, verbose_name='images/'),
        ),
    ]
