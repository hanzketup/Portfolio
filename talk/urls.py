from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.list),
    url('(?P<pk>\d+)/$', views.resolv),
    url('^projects$', views.listproject),
    url('^experiments$', views.listexp),

]
