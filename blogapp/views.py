from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    print(blogs)
    return render(request,'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.writer = request.GET['writer']
    blog.body = request.GET['body']
    blog.save()
    return redirect('/detail/' + str(blog.id))

def delete(request, del_blog_id):
    delete_post = get_object_or_404(Blog, pk=del_blog_id)
    delete_post.delete()
    return redirect('home')

def edit(request, edit_blog_id):
    edit_post = get_object_or_404(Blog, pk=edit_blog_id)
    return render(request, 'edit.html', {'post':edit_post})

def update(request, update_blog_id):
    update_post = get_object_or_404(Blog, pk=update_blog_id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('home')
