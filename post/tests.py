from django.test import TestCase
from .models import Article
from account.models import Profile
import unittest

# Create your tests here.


class ArticleTestCase(TestCase):
    def setUp(self):
        cat = Profile.objects.create(username='cat')
        Article.objects.create(title='who is this', description='this is alien', author=cat)

    def test_article_description(self):
        who = Article.objects.get(title='who is this')
        cat = Profile.objects.get(username='cat')
        self.assertEqual(who.description(), 'this is alien')
        self.assertEqual(who.author(), cat)


if __name__ == '__main__':
    unittest.main()