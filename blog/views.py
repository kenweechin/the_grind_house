from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post

def frontpage(request):
    # Get all the posts from the database
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})


def post_list(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)#
            comment.post = post
            comment.save()

            return redirect('post_list', slug=post.slug)
    else:
        form = CommentForm

    return render(request, 'blog/post_list.html', {'post': post, 'form': form})
