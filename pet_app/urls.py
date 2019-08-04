from django.urls import path
from .views import ListCatView


urlpatterns = [
    path('cats/', ListCatView.as_view(), name="cats-all")
]
