from django.conf.urls import  url
from django.contrib import admin
from curdapp import  views

urlpatterns = [
   url(r'^admin/',(admin.site.urls)),
    url(r'^$',views.home_view),
    url(r'^insert/',views.insert_view),
    url(r'^fetch/',views.fetch_view),
    url(r'^update/',views.update_view),
    url(r'^delete/',views.delete_view)

]
