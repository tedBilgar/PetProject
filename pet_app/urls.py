from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from pet_app import views
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

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', views.hello_world),
    path('cat-name-test/', views.add_suffix_for_catname),
    path('cat_dto_count/', views.cat_dto_count)
]

