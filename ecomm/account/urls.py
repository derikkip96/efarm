from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import (
	PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns =[
			url(r'register/$',views.userRegistration, name='register'),
			url(r'profile/edit/$',views.editProfile, name='editProfile'),
			url(r'login/$', views.loginView, name='logint'),
			url(r'logout/$', auth_views.logout, name='logout'),
			url(r'^password_change/$',views.PasswordChange, name='change'),

			url(r'^password_reset2/$',
				PasswordResetView.as_view(template_name='regist/password_reset_form.html'),
				name='reset1'),
			url(r'^password_reset/done/$',
				PasswordResetDoneView.as_view(template_name='regist/password_reset_done.html'),
				name='password_reset_done'),
			url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
				PasswordResetConfirmView.as_view(template_name='regist/password_reset_confirm.html'),
				name='password_reset_confirm'),
			url(r'^reset/done/$',
				PasswordResetCompleteView.as_view(template_name='regist/password_reset_complete.html'),
				name='password_reset_complete'),
			url(r'^profile/$',views.profileView, name='profilet')




]
