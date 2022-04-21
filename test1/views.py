from django.shortcuts import render
from test1.models import Post, Comment

# Create your views here.
def get_post(request):
    posts = Post.objects.all()
    return render(request, 'test1/post.html', {'posts': posts})

def get_comment(request):
    comments = Comment.objects.all()
    return render(request, 'test1/comment.html', {'comments': comments})