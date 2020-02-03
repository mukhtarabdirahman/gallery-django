from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.pics_of_day,name='picsToday'),
]