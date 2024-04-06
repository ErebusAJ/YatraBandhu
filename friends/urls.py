from django.urls import path
from . import views


urlpatterns = [
    path('travellers/', views.user_list, name="travellers"),
    path('interest/<int:to_user_id>/', views.send_interest, name='send-interest'),
]