from django.conf.urls import url
from django.views import generic
from django.views.generic.base import RedirectView
from django.contrib.sites.models import Site

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="http://"+Site.objects.get_current().domain+"/mederosblog/", permanent=True), name='home'),
    url(r'^humans.txt$', generic.TemplateView.as_view(template_name='mederoblog/humans.txt', content_type='text/plain'),
        name='humans'),
    url(r'^humans$', generic.TemplateView.as_view(template_name='mederoblog/humans.txt', content_type='text/plain'),
        name='humans'),
]
