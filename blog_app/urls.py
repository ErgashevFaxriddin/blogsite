from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import PostListView, post_detail


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>',
         post_detail,
         name='post_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)