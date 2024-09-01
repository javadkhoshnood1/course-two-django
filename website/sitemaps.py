from django.contrib.sitemaps import Sitemap
from blog.models import Post

# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home:index', 'website:contact']

    def location(self, items):
        return reverse(items)