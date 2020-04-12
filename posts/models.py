from django.db import models

from users.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)
    like_voters = models.ManyToManyField(User, related_name="like_voters")
    dislike_voters = models.ManyToManyField(User, related_name="dislike_voters")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created']

    def __str__(self):
        return f'{self.owner}: {self.body}'
