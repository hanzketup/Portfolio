from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.list),
    url('(?P<pk>\d+)/$', views.resolv),
    url('(?P<cat>\w+)/$', views.catlist),
    url('^projects$', views.listproject),
    url('^experiments$', views.listexp),

]
