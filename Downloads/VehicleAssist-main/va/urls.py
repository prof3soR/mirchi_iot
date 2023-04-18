"""va URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vehicle1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("login_view/",views.login_view,name="login_view"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logout_view,name="logout"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("mechanic_reg/",views.mechanic_registration,name="m_signup"),
    path("service_request/",views.srequest,name="srequest"),
    path("request_mechanic",views.request_mechanic,name="request_mechanic"),
    path("service_status",views.service_status,name="service_status"),
    path("mechanic_dashboard",views.mechanic_dashboard,name="mechanic_dashboard")
]
