import rest_framework_filters as filters
from .models import Cat
from .models import Owner
from .models import Toy


class CatFilter(filters.FilterSet):
    class Meta:
        model = Cat
        fields = {
            'name': ['exact', 'contains', 'in', 'icontains'],
            'home': ['contains']
        }


class OwnerFilter(filters.FilterSet):
    cat = filters.RelatedFilter(CatFilter, field_name='cat', queryset=Cat.objects.all())

    class Meta:
        model = Owner
        fields = {
            'name': ['exact', 'contains'],
            'money': ['exact']
        }


class ToyFilter(filters.FilterSet):
    cat = filters.RelatedFilter(CatFilter, field_name='cats', queryset=Cat.objects.all())

    class Meta:
        model = Toy
        fields = {
            'toy_name': ['exact', 'contains'],
            'developer': ['contains']
        }
