from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Tasks
from .serializers import SongsSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_task(title="", artist=""):
        if task_name != "" :
            Tasks.objects.create(title=title, artist=artist)



class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("tasks-all", kwargs={"version": "v1"})
        )
        print (response)
        # fetch the data from db
        expected = Tasks.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)