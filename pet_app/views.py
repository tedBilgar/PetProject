from .models import Cat
from .serializers import CatSerializer
from rest_framework import generics


class ListCatView(generics.ListAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
