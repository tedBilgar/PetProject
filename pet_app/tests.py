from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Cat
from .serializers import CatSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def createCat(name="", home=""):
        if name !="" and home !="":
            Cat.objects.create(name=name, home=home)

    def setUp(self):
        self.createCat("Alex", "Chelyabinsk")
        self.createCat("Boris", "Moscow"),
        self.createCat("Pushok", "Piter")


class GetAllCatTest(BaseViewTest):

    def test_get_all_cats(self):
        response = self.client.get(
            reverse("cats-all", kwargs={"version": "v1"})
        )

        expected = Cat.objects.all()
        serialized = CatSerializer(expected, many=True)
        self.assertTrue(response.data, serialized.data)
        self.assertTrue(response.status_code, status.HTTP_200_OK)



