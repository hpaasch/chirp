
from django.conf.urls import url, include  # added import
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),  # going to get url patterns and drop in. from django docs
    url(r'^$', views.IndexView.as_view(), name='index_view'),
    url(r'^chirp/(?P<pk>\d+)/$', views.ChirpDetailView.as_view(), name='chirp_detail_view'),
    url(r'^chirp/(?P<pk>\d+)/delete/$', views.ChirpDeleteView.as_view(), name='chirp_delete_view'),
    # url(r'^create_chirp/$', views.ChirpCreateView.as_view(), name='chirp_create_view'),
    url(r'^accounts/profile/$', views.ProfileUpdateView.as_view(), name='profile_update_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
