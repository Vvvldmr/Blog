from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm


def get_post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'blog/post_detail.html', {'post': post})


def create_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'blog/post_add.html', context={"form": form})

    if request.metod == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post_id = post.id)

    return render(request, 'blog/post_add.html', context={"form": form})