from django.urls import path
from .views import ProfileList,ProfileDetailView,follow_unfollow_profile
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ProfileList.as_view(),name = 'profile_list'),
    path('<pk>',ProfileDetailView.as_view(), name='profile-detail'),
    path('switch_follow/',follow_unfollow_profile,name = "follow-unfollow-view")
    # path('register/',views.register_user, name='register'),
    # path('',views.login_user,name='login_user'),
    # path('logout/',views.logout, name='logout'),
    # path('profile/<int:id>',views.user_profile,name='profile'),
    # # url(r'^profile/(?P<user_id>\d+)',views.profile, name='profile'),
    # path('image_detail/<int:id>',views.imagedetails,name='image_detail'),
    # path('post/',views.post,name = 'post_image'),
    # path('like/<int:pk>',views.LikeView,name='like_post'),
    # path('edit-profile/<int:pk>',ProfileUpdateView.as_view(),name='edit_profile')
    # # path('comment/<int:pk>',views.comment, name="comment"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)