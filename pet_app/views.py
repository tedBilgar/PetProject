from .models import Cat
from .models import Owner
from .models import Toy
from .serializers import CatSerializer
from .serializers import OwnerSerializer
from .serializers import ToySerializer

from rest_framework import viewsets


class CatViewSet(viewsets.ModelViewSet):

    serializer_class = CatSerializer
    queryset = Cat.objects.all()


class OwnerViewSet(viewsets.ModelViewSet):

    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class ToyViewSet(viewsets.ModelViewSet):

    serializer_class = ToySerializer
    queryset = Toy.objects.all()