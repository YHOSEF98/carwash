from django.urls import path, include
from rest_framework import routers
from user import views

router = routers.DefaultRouter()
router.register(r'permisos', views.PermissionViewSet)
router.register(r'grupos-usuarios', views.GroupViewSet)
router.register(r'usuarios', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls))
]