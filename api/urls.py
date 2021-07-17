from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$', views.index, name='index'),
    
    url('account/', include('django.contrib.auth.urls')),
]