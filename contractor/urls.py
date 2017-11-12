from django.conf.urls import include,url
from django.contrib.auth import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_complete, password_reset_confirm
from . import views
from django.core.urlresolvers import reverse_lazy
app_name = 'contractor'

urlpatterns = [
    # /contracts/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /contracts/<landscaper_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    url(r'^login/$', login, {'template_name' : 'contractor/login.html'}),

    url(r'^logout/$', logout, {'template_name' : 'contractor/logout.html'}),

    url(r'^register/$', views.register, name='register'),

    url(r'^profile/$', views.view_profile, name='profile'),

    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

    url(r'^profile/password/$', views.change_password, name='change_password'),

    url(r'^reset-password/$', password_reset,
        {'template_name': 'contractor/reset_password.html', 'post_reset_redirect': 'contractor:password_reset_done',
         'email_template_name': 'contractor/reset_password_email.html'}, name='reset_password'),

    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'contractor/reset_password_done.html'},
        name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'contractor/reset_password_confirm.html',
         'post_reset_redirect': 'contractor:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete,
        {'template_name': 'contractor/reset_password_complete.html'}, name='password_reset_complete')


]