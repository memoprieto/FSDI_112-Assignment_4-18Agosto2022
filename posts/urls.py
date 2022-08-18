from django.urls import path


urlpatterns = [
    path("", models.PostListView.as_view(), name="post_list"),
    path("new/", models.PostCreateView.as_view(), name="post_new"),
    path("<int:pk>/", models.PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/edit/", models.PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", models.PostDeleteView.as_view(), name="post_delete"),
]