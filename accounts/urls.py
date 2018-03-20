from django.urls import re_path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^login/$', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'),



    re_path(r'^reset/$',
            auth_views.PasswordResetView.as_view(
                template_name='accounts/password_reset.html',
                email_template_name='accounts/password_reset_email.html',
                subject_template_name='accounts/password_reset_subject.txt',
                success_url='/account/reset/done/'
            ),
            name='password_reset'),
    re_path(r'^reset/done/$',
            auth_views.PasswordResetDoneView.as_view(
                template_name='accounts/password_reset_done.html'),
            name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='accounts/password_reset_confirm.html'),
            name='password_reset_confirm'),
    re_path(r'^reset/complete/$',
            auth_views.PasswordResetCompleteView.as_view(
                template_name='accounts/password_reset_complete.html'),
            name='password_reset_complete'),


]
