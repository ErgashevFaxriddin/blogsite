# from django.shortcuts import render, get_object_or_404
# from .models import Post
# from .forms import CommentForm
# from django.views.generic import ListView
#
#
# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 5
#     template_name = "blog/post/list.html"
#
#
# def post_detail(request, year, month, day, slug):
#     post = get_object_or_404(
#         Post,
#         slug=slug,
#         status='published',
#         publish__year=year,
#         publish__month=month,
#         publish__day=day
#     )
#     comments = post.comments.filter(active=True)
#     form = CommentForm()
#
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#
#     return render(request, 'blog/post/detail.html', {
#         'post': post,
#         'comments': comments,
#         'form': form
#     })


from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from .models import Post
from .forms import CommentForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'


class PostDetailView(View):
    def get(self, request, year, month, day, slug):
        post = get_object_or_404(
            Post,
            slug=slug,
            status='published',
            publish__year=year,
            publish__month=month,
            publish__day=day,
        )
        comments = post.comments.filter(active=True)
        form = CommentForm()

        return render(request, 'blog/post/detail.html', {
            'post': post,
            'comments': comments,
            'form': form,
            'comment_count': comments.count(),
        })

    def post(self, request, year, month, day, slug):
        post = get_object_or_404(
            Post,
            slug=slug,
            status='published',
            publish__year=year,
            publish__month=month,
            publish__day=day,
        )

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # Muvaffaqiyatli qo'shilgandan keyin redirect (PRG)
            return redirect('blog:post_detail',
                            year=year, month=month, day=day, slug=slug)

        # Form xato bo'lsa, qayta ko'rsatamiz
        comments = post.comments.filter(active=True)
        return render(request, 'blog/post/detail.html', {
            'post': post,
            'comments': comments,
            'form': form,
            'comment_count': comments.count(),
        })