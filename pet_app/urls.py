from django.urls import path
from .views import CatViewSet
from .views import OwnerViewSet
from .views import ToyViewSet
from .views import CatToySet
from rest_framework.routers import DefaultRouter

app_name = "cats"

router = DefaultRouter()
router.register(r'cats', CatViewSet, base_name='user')
router.register(r'owners', OwnerViewSet, base_name='user')
router.register(r'toys', ToyViewSet, base_name='user')
router.register(r'cat-toy', CatToySet, base_name='user')

urlpatterns = router.urls