from django.urls import path
from .views import CatViewSet
from rest_framework.routers import DefaultRouter

app_name = "cats"

router = DefaultRouter()
router.register(r'cats', CatViewSet, base_name='user')

urlpatterns = router.urls