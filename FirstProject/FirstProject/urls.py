from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^articles/', include('articles.urls')),
    re_path('about/$', views.about),
    re_path('$', views.homepage),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)