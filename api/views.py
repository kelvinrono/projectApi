from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import ProfileForm,UpdateUserForm,UpdateUserProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def profile(request, username):
    images = request.user.profile.images.all()
    print(images)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,
    }
    return render(request, 'profile.html', params)

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('profile')
 
    return render(request,'edit_profile.html',{"form":form})
