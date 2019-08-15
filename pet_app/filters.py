import rest_framework_filters as filters
from .models import Cat


class CatFilter(filters.FilterSet):
    class Meta:
        model = Cat
        fields = {
            'name': ['exact', 'contains', 'in', 'icontains'],
            'home': ['contains']
        }
