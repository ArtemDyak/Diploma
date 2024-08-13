from django.urls import path
from . import views


urlpatterns = [
    path('title/', views.ForumTitleView.as_view(), name='title_forum'),
    path('new/', views.MessageCreateView.as_view(), name='new_forum'),
]
