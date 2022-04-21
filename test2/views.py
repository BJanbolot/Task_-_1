from django.shortcuts import render

# Create your views here.
def get_post(request):
    return render(request, 'test2/post.html')

def get_comment(request):
    return render(request, 'test2/comment.html')