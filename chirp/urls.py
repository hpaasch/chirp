
from django.conf.urls import url, include  # added import
from django.contrib import admin

from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),  # going to get url patterns and drop in. from django docs
    url(r'^$', views.IndexView.as_view(), name='index_view'),
    url(r'^chirp/(?P<pk>\d+)/$', views.ChirpDetailView.as_view(), name='chirp_detail_view'),
    url(r'^create_chirp/$', views.ChirpCreateView.as_view(), name='chirp_create_view'),

]
