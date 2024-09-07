"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from core.settings import COMINGSOON,MEDIA_URL,MEDIA_ROOT
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from django.views.generic import TemplateView
sitemaps = {
    'static': StaticViewSitemap,
    'blog' : BlogSitemap
    
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("home.urls")),
    path("blogs/",include("blog.urls")),
    path("",include("website.urls")),
    path("accounts/",include("accounts.urls")),
    # ...
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),


]+ static(MEDIA_URL, document_root=MEDIA_ROOT)

if COMINGSOON:
    urlpatterns.insert(
        0, re_path(r"^", TemplateView.as_view(template_name="comingsoon.html"))
    )