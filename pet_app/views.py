from .models import Cat
from .serializers import CatSerializer

from rest_framework import viewsets


class CatViewSet(viewsets.ModelViewSet):

    serializer_class = CatSerializer
    queryset = Cat.objects.all()