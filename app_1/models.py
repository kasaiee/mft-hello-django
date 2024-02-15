from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=70, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title