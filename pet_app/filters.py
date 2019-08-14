import django_filters
from .models import Cat


class CatFilter(django_filters.FilterSet):
    class Meta:
        model = Cat
        fields = {'name': ['contains']}
