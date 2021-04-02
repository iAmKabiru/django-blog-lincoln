from django.shortcuts import render
from blog.models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})