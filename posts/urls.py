from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("new/", views.PostCreateView.as_view(), name="post_new"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
]

# from django.urls import path
# from posts import models


# urlpatterns = [
#     path("", models.PostListView.as_view(), name="post_list"),
#     path("new/", models.PostCreateView.as_view(), name="post_new"),
#     path("<int:pk>/", models.PostDetailView.as_view(), name="post_detail"),
#     path("<int:pk>/edit/", models.PostUpdateView.as_view(), name="post_edit"),
#     path("<int:pk>/delete/", models.PostDeleteView.as_view(), name="post_delete"),
# ]