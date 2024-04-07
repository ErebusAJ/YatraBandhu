from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, TravelPlanForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from friends.models import Friendship


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form,
    }
    return render(request, 'users/update.html', context)


def landing(request):
    return render(request, 'users/landing.html')


def home(request):
    if request.method == 'POST':
        form = TravelPlanForm(request.POST)
        if form.is_valid():
            travel_plan = form.save(commit=False)
            travel_plan.user = request.user  
            travel_plan.save()  
            # Get the selected location from the form
            location = form.cleaned_data.get('location')
            print(location)
            # Pass the selected location to the template
            return render(request, 'users/trip_plan.html', {'form': form, 'location': location})
    else:
        form = TravelPlanForm()
    return render(request, 'users/home.html', {'form': form})

def contact(request):
    return render(request, 'users/contact.html')


# Profile 

@login_required
def profile(request):
    user = request.user
    received_requests = Friendship.objects.filter(to_user=request.user)
    context = {
        'user': user,
        'received_requests': received_requests,
    }
    return render(request, 'users/profile.html', context)


@login_required
def send_friend_request(request, to_user_id):
    to_user = get_object_or_404(User, pk=to_user_id)
    Friendship.objects.create(from_user=request.user, to_user=to_user)
    return redirect('profile')  # Redirect to the user's profile page

@login_required
def accept_friend_request(request, friendship_id):
    friendship = get_object_or_404(Friendship, pk=friendship_id)
    friendship.accepted = True
    friendship.save()
    return redirect('profile')  # Redirect to the user's profile page

@login_required
def reject_friend_request(request, friendship_id):
    friendship = get_object_or_404(Friendship, pk=friendship_id)
    friendship.delete()  # Or mark it as rejected if you want to keep the record
    return redirect('profile')  # Redirect to the user's profile page


def trip(request):
    return render(request, 'users/trip_plan.html')
