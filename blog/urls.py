from django.urls import path, re_path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.post_list, name="post_list"),
    re_path(r'detail/(?P<post>[-\w]+)/', views.post_detail, name="post_detail"),
]

#<int:year>/<int:month>/<int:day>/