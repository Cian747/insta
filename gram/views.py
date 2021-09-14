from django.shortcuts import render,redirect,get_object_or_404
from .forms import InstaRegistrationForm,EditForm,PostImageForm,CommentForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Image,Comment
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from itertools import chain
from .email import send_welcome_email

# Create your views here.
def register_user(request):
    rgf = InstaRegistrationForm()
    if request.method == 'POST':
        rgf = InstaRegistrationForm(request.POST)
        if rgf.is_valid():
            rgf.save()
            user = rgf.cleaned_data.get('username')
            email = rgf.cleaned_data.get('email')
            # send_welcome_email(user,email)
            messages.success(request, 'Account was created for ' + user)
            return redirect('login_user')
    
    return render(request, 'registration/registration_form.html', {'rgf': rgf})

def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'registration/login.html')

def logout(request):
    return redirect('login_user')

class HomeView(ListView):
    models = Image
    template_name = 'index.html'

    def get_queryset(self): 
        return Image.objects.all()

class ProfileUpdateView(UpdateView):
    models = Profile
    form_class = EditForm
    template_name = 'profile/edit-profile.html'

    def get_queryset(self): 
        return Profile.objects.all()


def posts_of_following_profiles(request):
    # get logged in user
    profile = Profile.objects.get(user=request.user)
    # check who you are following
    users = [user for user in profile.following.all()]
    # initial values for variables
    posts = []
    qs = None
    # get post for people who you are following
    for u in users:
        p = Profile.objects.get(user=u)
        p_posts = p.image_set.all()
        
        posts.append(p_posts)      
    my_posts = profile.image_posts()
    posts.append(my_posts)

    user = request.user

    # sort and chain querysets and unpack the posts lists
    if len(posts)>0:
        qs = sorted(chain(*posts), reverse=True, key=lambda obj:obj.created)

    return render(request,'posts/index.html',{"profile":profile,"posts":qs,"user":user})


def edit_profile(request,id):
    editing_profile = Profile.objects.get(id=id)
    form = EditForm
    # current_user = request.user
    if request.method == 'POST':
        form = EditForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = editing_profile.user.id
            post.save()
            return redirect(request.META.get('HTTP_REFERER'))

    return render(request,'profile/edit-profile.html',{"form":form})


def imagedetails(request,id):
    current_image = Image.objects.get(id=id)
    comments = Comment.objects.filter(image = id).all()

    # stuff = get_object_or_404(Image, id = request.POST.get('id'))
    total_likes = current_image.total_likes()

    current_user = request.user
    com_form = CommentForm()
   
    if request.method == 'POST':
        new_comment = Comment(comment = request.POST.get('comment'), user_id=current_user, image = Image.objects.get(id=id))
        new_comment.save()
        return HttpResponseRedirect(reverse('image_detail', args=[int(id)]))


    return render(request,'image-detail.html',{"com_form":com_form,"object":current_image,"total_likes":total_likes,"comments":comments,"user":current_user})

            
# For like you could pull up a modal that generates the like
def LikeView(request,pk):
    image_post = get_object_or_404(Image, pk=request.POST.get('post_id'))
    image_post.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))

class PostImageView(CreateView):
    models = Image
    form_class = PostImageForm
    template_name = 'post_image.html'

def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostImageForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('index')
    
    else:
        form = PostImageForm()

    title = 'Instagram - Post Image'
    return render(request,'post_image.html',{"form":form, "title":title})

def user_profile(request,id):
    user_profile = Profile.objects.get(id = id)
    user_profile_images = Image.objects.filter(profile = id).all()

    current_user = request.user.id

    my_profile = Profile.objects.get(user =request.user)
    if user_profile.user in my_profile.following.all():
        follow = True
    else:
        follow = False


    return render(request,'profile/profile.html', {"profile":user_profile,"images":user_profile_images,"follow":follow,"current_user":current_user})

def search_for_user(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        search_results = Profile.search_by_user(search_term)

        return render(request,'search.html',{"results":search_results})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})


        


