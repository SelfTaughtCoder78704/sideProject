from django.conf.urls import url

from . import views

app_name = 'contractor'

urlpatterns = [
    # /contracts/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /contracts/<landscaper_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
]