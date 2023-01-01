"""drfTutorial URL Configuration

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
from django.urls import path, include

from quickstart import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls), # 서버주소/admin 이라는 url 요청을 관리자 page로 연결.
    # path('', include(router.urls)), # router class 내의 urls.py의 url로 연결.
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('admin/', admin.site.urls),
    path('', include('gistHelper.urls')),
]
