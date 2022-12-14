from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("/post/<int:post_id>/", 
        views.PostDetailListView.as_view(),
        name="post-detail",
        ),
    path("/posts/new/",
        views.PostCreateView.as_view(),
        name="post-create",
        ),
    path("/posts/<post_id>/edit",
        views.PostUpdateView.as_view(),
        name="post-update"),
    path("/posts/<post_id>/delete/",
        views.PostDeleteView.as_view(),
        name="post-delete")
]
