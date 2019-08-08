from rest_framework import serializers
from pet_app.models import Cat
from pet_app.models import Owner


class CatSerializer(serializers.ModelSerializer):
    owners_of_cat = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cat
        fields = ("name", "home", 'owners_of_cat')


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('cat', 'name', 'money', 'occupation')