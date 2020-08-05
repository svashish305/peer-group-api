from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    re_path('api/', include('peergroup.urls'))
]