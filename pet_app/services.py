from .models import Cat
from .serializers import CatSerializer
from .dtos import CatDTO
from django.core import serializers
import json
import simplejson
from django.db.models import Q


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

    '''
    Пример сериализации объекта(списка) в JSON
    '''
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

    '''
    Пример получения JSON. Десериализация в объект.
    '''
    @staticmethod
    def post_test_parse_cats(request):
        print(request.data)
        to_json = simplejson.dumps(request.data, namedtuple_as_object=True)
        data = json.loads(to_json)
        cats = Cat.objects.filter(
            Q(name=data['name']) | Q(home__startswith=data['home'])
        )
        serializer = CatSerializer(cats, many=True)
        return serializer.data
