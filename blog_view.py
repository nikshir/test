posts_base = {post['id']:post for post in posts}

def post_detail(request, post_id):
    template = 'blog/detail.html'
    if post_id not in posts_base.keys():
        raise Http404(ERROR_404_POST_DETAIL.format(post_id=post_id))
    context = {'post': posts_base['post_id']}
    return render(request, template, context)
