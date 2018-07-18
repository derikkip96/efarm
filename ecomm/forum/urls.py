from django.conf.urls import url
from . views import postView,\
                    postDetails,PostLikeToggle,\
                    PostLikeApi
from . import views

urlpatterns=[
                url(r'post/',views.postView, name='postview'),
                url(r'^(?P<post_id>\d+)/$',views.postDetails,name='post_details'),

                url(r'^(?P<id>\d+)/like/$',PostLikeToggle.as_view(),name='postlike'),
                url(r'^api/(?P<id>\d+)/like/$',PostLikeApi.as_view(),name='postlikeapi'),
                url(r'^question/(?P<quiz_id>\d+)/details/$',views.qdetail, name='quest'),


]