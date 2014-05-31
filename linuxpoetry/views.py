"""Simply displays a page and retrieves poems."""

from django.shortcuts import render_to_response
from linuxpoetry.models import Post, BlogPost


def index(request, post_id=None, blog=False):
    """Will return an index page."""
    post = None
    next_id = None
    prev_id = None
    post_qs = Post.objects
    template_name = 'linuxpoetry/base.html'
    if blog is True:
        post_qs = BlogPost.objects
        template_name = 'linuxpoetry/blog.html'

    post_count = post_qs.count()
    if post_count > 0:
        if not post_id:
            post = post_qs.order_by('-created_at')[0]
        else:
            post = post_qs.get(id=post_id)
        if post.id < post_count:
            next_id = post.id + 1
        if post.id > 1:
            prev_id = post.id - 1

    return render_to_response(
        template_name,
        {
            'request': request,
            'post': post,
            'next_id': next_id,
            'prev_id': prev_id,
        }
    )


def blogindex(request, post_id=None):
    return index(request, post_id, True)
