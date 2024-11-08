from django.urls import path, include
from rest_framework import routers
from api import views
from .views import CategoryListAPIView

#importar las view
router=routers.DefaultRouter()
router.register(r'company', views.CompanyViewSet)
# router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'client', views.ClientViewSet)
router.register(r'sale', views.SaleViewSet)
router.register(r'detsale', views.DetSaleViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('categoria/listado/', CategoryListAPIView.as_view(), name="listado_categoria"),
]