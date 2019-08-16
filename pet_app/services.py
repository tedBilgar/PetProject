from .models import Cat
from .serializers import CatSerializer


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
