from django.db import models


# Create your models here.
class TimeStameModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(TimeStameModel):
    author = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.CASCADE,
        related_name="post_author",
    )
    image = models.ImageField(blank=True)
    cpation = models.TextField(blank=True)
    image_likes = models.ManyToManyField(
        "users.User",
        related_name="post_likes",
    )


class Comment(TimeStameModel):
    author = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.CASCADE,
        related_name="comment_author",
    )
    posts = models.ForeignKey(
        Post,
        null=True,
        on_delete=models.CASCADE,
        related_name="comment_post",
    )
    contents = models.TextField(blank=True)
