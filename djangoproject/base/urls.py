from django.conf.urls.defaults import url, include, patterns

urlpatterns = patterns('djangoproject.base.views',
    url(r'^$', 'home', name='home'),
)
