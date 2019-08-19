from django.db import models
from account.models import Profile

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(
        to=Profile,
        on_delete=models.SET_NULL,
        null=True
    )

    title = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='title'
    )

    description = models.TextField(
        blank=True,
        verbose_name='description'
    )

    like = models.IntegerField(blank=True, default=0)
    unlike = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title