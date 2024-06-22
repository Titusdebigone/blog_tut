from django.urls import path
from .views import PostListAPIView

app_name = "posts"

urlpatterns = [
    path('list/', PostListAPIView.as_view())
]