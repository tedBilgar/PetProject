from .models import Cat
from .serializers import CatSerializer
from .dtos import CatDTO
from django.core import serializers
import simplejson as json


class CatService(object):
    @staticmethod
    def get_len_of_cats():
        cats = Cat.objects.all()
        cat_len = len(cats)
        return cat_len

    @staticmethod
    def change_name_by_home(home_check):
        cats = Cat.objects.filter(
            home=home_check
        )
        for cat in cats:
            cat.name += 'Test'
        serializer = CatSerializer(cats, many=True)
        return serializer

    @staticmethod
    def get_cat_and_count():
        cats = Cat.objects.all()
        catdto_list = []
        count = 0
        for cat in cats:
            catdto_list.append(CatDTO(cat.name, cat.home, count))
            count += 1
        data = json.dumps(catdto_list, namedtuple_as_object=True)
        return data
