from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [

    path('admin/',admin.site.urls),
    path('sad/',views.deb),
    path('add/',views.debu),
    path('list/',views.student.as_view()),
    path('createadd/',views.studentcreate.as_view()),
]
