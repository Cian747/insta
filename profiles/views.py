from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import Profile

# Create your views here.

def follow_unfollow_profile(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user = request.user)
        pk = request.POST.get('profile_pk')
        print(pk)
        obj = Profile.objects.get(pk = pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
            my_profile.save()
        else:
            my_profile.following.add(obj.user)
        
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('profile')

class ProfileList(ListView):
    model = Profile
    template_name = 'profile/main-profile.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().exclude(user = self.request.user)

def all_profiles(request):
    profiles = Profile.objects.all()
    print(profiles)
    return render(request,'profile/main-profile.html',{"profiles":profiles})

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile.html'
    context_object_name = 'profile'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user = self.request.user)
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        context["follow"] =  follow
        return context


    

