from django.urls import path, include
from rest_framework import routers
from api import views

#importar las view
router=routers.DefaultRouter()
router.register(r'company', views.CompanyViewSet)


urlpatterns = [
    path('', include(router.urls))
]