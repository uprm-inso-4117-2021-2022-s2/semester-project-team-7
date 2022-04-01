from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('browse', views.browse),
    path('search', views.search),
    path('course', views.viewCourse),
    path('vote', views.upvote),
    path('submitfeedback', views.submitfeedback),
    path('renderfeedback', views.renderfeedback),
    path('deletefeedback', views.deletefeedback),
    path('myfeedback', views.myFeedback),
    path('user', views.user),
    path('requestpermission/', views.requestpermission),
    path('permissionrequests/', views.permissionrequests),
    path('adminpanel/requests/', views.adminpanel_requests),
    path('approverequest/', views.approverequest),
    path('rejectrequest/', views.rejectrequest)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)