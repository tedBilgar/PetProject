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
from .filters import CatFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_filters.backends import RestFrameworkFilterBackend


class CatViewSet(viewsets.ModelViewSet):

    serializer_class = CatSerializer
    queryset = Cat.objects.all()
    filter_backends = [RestFrameworkFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name', 'home']
    filter_class = CatFilter


class OwnerViewSet(viewsets.ModelViewSet):

    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()
    ordering = ['name', 'money']


class ToyViewSet(viewsets.ModelViewSet):

    serializer_class = ToySerializer
    queryset = Toy.objects.all()


class CatToySet(viewsets.ModelViewSet):

    serializer_class = CatToySerializer
    queryset = CatToyRelation.objects.all()


'''
http://127.0.0.1:8000/api/v1/cats/?name__contains=Bo&home__contains=Chelyabinsk&ordering=name
Так например фильтруются имена по собстрингу Bo, home сабстрингу Chelyabinsk, и сортировки по имени по убыванию.
Если нужна обратная сортировка то нужно поставить ordering=-name.

Если нужна регистро независимость, то http://127.0.0.1:8000/api/v1/cats/?name__icontains=bo
name__icontains добавлена.icontains добавляется в сам фильтр в FilterSet в filters.py.

'''