from operator import mod
from pyexpat import model
from tkinter import CASCADE
from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to= 'blog_photo')
    date = models.DateTimeField(auto_now_add=True) # 지금 시간을 추가

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True) 
    # 어떤 게시물에 달려있는 댓글인지 알 수 있는, 댓글이 달린 그 게시물이 쓰여진다.
    # 댓글이 달린 게시물이 삭제될 시 댓글도 같이 삭제되도록 on_delete = models.CASCADE 를 해준다.
    post = models.ForeignKey(Blog, on_delete=models.CASCADE) 

    def __str__(self):
        return self.comment