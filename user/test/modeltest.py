import unittest

from django.test import TestCase
from django.utils import timezone
from login.user.models import UserProfile


class UserProfileTest(unittest.TestCase):

    def create_userprofile(self, first_name="sagar", last_name="mundkar", username='sagarmundkar'):
        return UserProfile.objects.create(first_name=first_name, last_name=last_name, username=username,
                                          created_at=timezone.now())

    def test_userprofile_creation(self):
        w = self.create_userprofile()
        self.assertTrue(isinstance(w, UserProfile))
        self.assertEqual(w.__unicode__(), w.first_name)


