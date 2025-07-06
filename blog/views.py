from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def get_post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'blog/post_detail.html', {'post': post})


def create_post(request):
    if request.method == "GET":
        return render(request, 'blog/post_add.html')
    
    if request.method == "POST":
        user_title = request.POST.get('title').strip()
        user_text = request.POST.get('text').strip()

        errors_dict = {}

        if not user_title:
            errors_dict['title'] = 'Обязательное поле'
        if not user_text:
            errors_dict['text'] = 'Обязательное поле'

        if not errors_dict:
            post = Post.objects.create(title = user_title, content = user_text)
            return redirect('post_detail', post_id = post.id)
        else:
            context = {
                'errors': errors_dict,
                'title': user_title,
                'text': user_text,
            }
            return render(request, 'blog/post_add.html', context=context)