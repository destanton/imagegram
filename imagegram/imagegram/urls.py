"""imagegram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from image_app.views import ImageListView, UserCreateView, ImageCreateView, ImageUpdateView,\
                            ImageDeleteView, CommentCreateView, ImageDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', ImageListView.as_view(), name="image_list_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^create/$', ImageCreateView.as_view(), name="image_create_view"),
    url(r'^image/(?P<pk>\d+)/$', ImageDetailView.as_view(), name="image_detail_view"),
    url(r'^update/(?P<pk>\d+)/$', ImageUpdateView.as_view(), name="image_update_view"),
    url(r'^delete/(?P<pk>\d+)/$', ImageDeleteView.as_view(), name="image_delete_view"),
    url(r'^comment/(?P<pk>\d+)/$', CommentCreateView.as_view(), name="image_comment_view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
