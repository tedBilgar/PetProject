from .models import Cat
from .serializers import CatSerializer


class CatService(object):
    @staticmethod
    def get_len_of_cats():
        cats = Cat.objects.all()
        cat_len = len(cats)
        return cat_len
