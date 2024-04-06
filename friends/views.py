from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Friendship
from users.models import TravelPlan
from django.contrib.auth.decorators import login_required


@login_required
def user_list(request):
    users = User.objects.all()
    travel = TravelPlan.objects.all()
    friendships = Friendship.objects.filter(from_user=request.user)
    return render(request, 'friends/user_list.html', {'users': users, 'friendships': friendships, 'plans': travel})


@login_required
def send_interest(request, to_user_id):
    to_user = User.objects.get(pk=to_user_id)
    if request.method == 'POST':
        # Process the form submission
        # For example, create a friendship request
        friendship = Friendship.objects.create(from_user=request.user, to_user=to_user)
        return redirect('travellers')
    else:
        return render(request, 'friends/send_interest.html', {'to_user': to_user})
    

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
