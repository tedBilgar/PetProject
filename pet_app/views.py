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
from .filters import OwnerFilter
from .filters import ToyFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_filters.backends import RestFrameworkFilterBackend
from rest_framework.pagination import LimitOffsetPagination


class CatViewSet(viewsets.ModelViewSet):

    serializer_class = CatSerializer
    queryset = Cat.objects.all()
    filter_backends = [RestFrameworkFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name', 'home']
    filter_class = CatFilter
    pagination_class = LimitOffsetPagination


class OwnerViewSet(viewsets.ModelViewSet):

    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()
    filter_backends = [RestFrameworkFilterBackend, filters.OrderingFilter]
    ordering = ['name', 'money']
    filter_class = OwnerFilter


class ToyViewSet(viewsets.ModelViewSet):

    serializer_class = ToySerializer
    queryset = Toy.objects.all()
    filter_backends = [RestFrameworkFilterBackend, filters.OrderingFilter]
    ordering = ['toy_name', 'developer']
    filter_class = ToyFilter


class CatToySet(viewsets.ModelViewSet):

    serializer_class = CatToySerializer
    queryset = CatToyRelation.objects.all()


'''
http://127.0.0.1:8000/api/v1/cats/?name__contains=Bo&home__contains=Chelyabinsk&ordering=name
Так например фильтруются имена по собстрингу Bo, home сабстрингу Chelyabinsk, и сортировки по имени по убыванию.
Если нужна обратная сортировка то нужно поставить ordering=-name.

Если нужна регистро независимость, то http://127.0.0.1:8000/api/v1/cats/?name__icontains=bo
name__icontains добавлена.icontains добавляется в сам фильтр в FilterSet в filters.py.

Пагинация через LimitOffsetPagination выполняется через как http://127.0.0.1:8000/api/v1/cats/?limit=2&offset=2 , где 
есть лимит, и с какого элемента мы начинаем считать (именно с элемента, а не куска в виде лимита). Ответ приходит в виде:
{
    "count": 3,
    "next": null,
    "previous": "http://127.0.0.1:8000/api/v1/cats/?limit=2",
    "results": [
        {
            "id": 3,
            "name": "Lenya",
            "home": "Peter",
            "owners_of_cat": []
        }
    ]
}

TODO посмотреть с числами (больше, меньше, равно) и датами (раньше, позднее)

'''