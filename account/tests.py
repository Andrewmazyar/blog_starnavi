from django.test import TestCase
from account.models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(username="lion")
        Profile.objects.create(username="cat")

    def test_user_existing(self):
        lion = Profile.objects.get(username="lion")
        cat = Profile.objects.get(username="cat")
        self.assertEqual(lion.username(), "lion")
        self.assertEqual(cat.username(), "cat")