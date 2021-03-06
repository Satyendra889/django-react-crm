from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'sales-person', views.SalesPersonView)
router.register(r'leads', views.LeadView)


urlpatterns = [
    path('', include(router.urls)),
]