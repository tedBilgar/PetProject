from .models import Cat
from .models import Owner
from .models import Toy
from .models import CatToyRelation
from .serializers import CatSerializer
from .serializers import OwnerSerializer
from .serializers import ToySerializer
from .serializers import CatToySerializer

from rest_framework import viewsets

from rest_framework import filters


class CatViewSet(viewsets.ModelViewSet):

    serializer_class = CatSerializer
    queryset = Cat.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'home']
    ordering_fields = ['name', 'home']


class OwnerViewSet(viewsets.ModelViewSet):

    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class ToyViewSet(viewsets.ModelViewSet):

    serializer_class = ToySerializer
    queryset = Toy.objects.all()


class CatToySet(viewsets.ModelViewSet):

    serializer_class = CatToySerializer
    queryset = CatToyRelation.objects.all()
