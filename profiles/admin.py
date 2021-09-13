from django.contrib import admin
from .models import Profile
from gram.models import Image,Comment
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('')
admin.site.register(Profile)