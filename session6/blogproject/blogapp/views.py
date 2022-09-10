from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

# Create your views here.
def home(request):
    # 블로그 글들을 모두 띄우는 코드
    posts = Blog.objects.all() # 블로그 객체들을 DB에서 가져 오게 된다.
    return render(request, 'index.html', {'posts':posts})

def new(request):
    return render(request, 'new.html')

def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

# django form을 이용해서 입력값을 받는 함수
# GET 요청과 (= 입력값을 받을 수 있는 html을 갖다 줘야함)
# POST 요청 (= 입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리)
# 둘 다 처리가 가능한 함수
def formcreate(request):
    if(request.method == 'POST'):
        # 입력 내용을 DB에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            # 저장하는 코드
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save() # 데이터베이스에 저장
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 갖다주기
        form = BlogForm() # 객체 생성
    return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
    if(request.method == 'POST' or request.method == 'FILES'):
        # 입력 내용을 DB에 저장
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            # 저장하는 코드
            form.save()
            return redirect('home')
    else:
        # 입력을 받을 수 있는 html을 갖다주기
        form = BlogModelForm() # 객체 생성
    return render(request, 'form_create.html', {'form':form}) 

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 갖고 와서
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # blog_id 번째 블로그 글을 detail.html로 띄워주는 코드

    comment_form = CommentForm()

    return render(request, 'detail.html', {'blog_detail' : blog_detail, 'comment_form' : comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False) # filled_form을 일단은 저장하지 않고 대기해라
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()

    return redirect('detail', blog_id)