from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    # 내가 입력 받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__' # blog class 안에 있는 title, body 데이터가 전부 다 form의 대상이 됨
        # fields = ['title', 'body'] 특정 특성만 이용하고 싶을 때는 list 형식으로

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['comment']