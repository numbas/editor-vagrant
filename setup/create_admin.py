from django.contrib.auth.models import User
from accounts.models import UserProfile

u = User.objects.create_user('admin',password='admin')
u.is_superuser = True
u.is_staff = True
u.first_name = "Admin"
u.last_name = "van Buuren"
u.save()
