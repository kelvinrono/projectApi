from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
]
