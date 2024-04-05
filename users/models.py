from django.contrib.auth.models import User

class user(User):
    
    def __str__(self):
        return self.username
