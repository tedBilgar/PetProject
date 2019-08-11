from rest_framework import serializers
from pet_app.models import Cat
from pet_app.models import Owner
from pet_app.models import Toy
from pet_app.models import CatToyRelation


class CatSerializer(serializers.ModelSerializer):
    owners_of_cat = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cat
        fields = ("name", "home", 'owners_of_cat')


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('cat', 'name', 'money', 'occupation')


class ToySerializer(serializers.ModelSerializer):

    class Meta:
        model = Toy
        fields = ('toy_name', 'developer')


class CatToySerializer(serializers.ModelSerializer):

    class Meta:
        model = CatToyRelation
        fields = ('cat', 'toy', 'major')


