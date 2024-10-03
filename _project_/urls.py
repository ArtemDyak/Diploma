from django.contrib import admin
from django.urls import path, include
from .views import TitleViewRedirect
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("apps.users.urls")),
    path('forum/', include('apps.forum.urls')),
    path('', TitleViewRedirect.as_view())
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
