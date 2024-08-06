from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.ForumTitleView.as_view(), name='title_forum')
]