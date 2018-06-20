from django.conf.urls import url
from . views import postView,PostLikeToggle
from . import views

urlpatterns=[
                url(r'post/',views.postView, name='postview'),
                url(r'^(?P<post_id>\d+)/$',views.postDetails,name='post_details'),
                url(r'^(?P<id>\d+)/like/$',PostLikeToggle.as_view(),name='postlike'),
                url(r'post/question/(?P<Q_id>\d+)/$',views.QuestionDetails,name='question')
]