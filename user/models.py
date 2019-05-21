from django.contrib.auth.models import User
from django.db import models


# Create your models her


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)


def __str__(self):
    return self.uesrname
