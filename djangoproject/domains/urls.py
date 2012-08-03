from django.conf.urls import url, patterns
from djangoproject.domains import views

urlpatterns = patterns('djangoproject.domains.views',
    url(r'^oldest$', views.OldDomainListView.as_view(), name='domains_oldest'),
)
