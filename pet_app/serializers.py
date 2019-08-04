from rest_framework import serializers
from pet_app.models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ("name", "home")
