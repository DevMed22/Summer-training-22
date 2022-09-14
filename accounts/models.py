from django.db import models
from django.contrib.auth.models import User
# Create your models here.


User._meta.get_field('email')._unique = True

User._meta.get_field('username')._unique = True
