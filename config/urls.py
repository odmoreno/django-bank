from django.conf import settings
from django.contrib import admin
from django.urls import path
from core_apps.user_auth.views import TestLoggingView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", TestLoggingView.as_view(), name="home"),
]
