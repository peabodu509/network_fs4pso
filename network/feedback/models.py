from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    subject = models.CharField(max_length=20, verbose_name='과목')
    created_date = models.DateTimeField(auto_now=True)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.subject)

class Post(models.Model):
    subject = models.ForeignKey('feedback.Subject', default=1, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goodPoint = models.TextField(verbose_name='좋았던 점', default=' ')
    improvingPoint = models.TextField(verbose_name='개선되었으면 하는 점', default=' ')
    anotherPoint = models.TextField(verbose_name='하고싶은 말', default=' ')
    created_date = models.DateTimeField(auto_now=True)
    numOfLike = models.IntegerField(default=0)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user)

class Comment(models.Model):
    post = models.ForeignKey('feedback.Post', on_delete=models.CASCADE)
    user = models.CharField(verbose_name="작성자", max_length=256)
    commentDesc = models.TextField(verbose_name='댓글', default=' ')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.commentDesc)

class Like(models.Model):
    post = models.ForeignKey('feedback.Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    isUserLiked = models.DateTimeField(auto_now_add=True)