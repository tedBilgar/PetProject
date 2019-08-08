from .models import Cat
from .models import Owner
from .serializers import CatSerializer
from .serializers import OwnerSerializer

from rest_framework import viewsets


class CatViewSet(viewsets.ModelViewSet):

    serializer_class = CatSerializer
    queryset = Cat.objects.all()


class OwnerViewSet(viewsets.ModelViewSet):

    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()