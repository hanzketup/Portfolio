from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.home),

    url('^logout$', views.dashout),

    url('^articles$', views.dashlist),
    url('^articles/(?P<pk>\d+)$', views.dashart),
    url('^articles/new$', views.dashnew),


]