from django.shortcuts import render
from app_1.models import Post


def post_list(request):
    post_list = Post.objects.filter(is_published=True)
    return render(request, 'index.html', {'post_list': post_list})