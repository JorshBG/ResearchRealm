from django.test import TestCase

from ScholarStack.models import Thesis
from django.contrib.auth.models import User


# Create your tests here.
class TestScholarStack(TestCase):

    def setUp(self):
        file = open("testfile.txt", "w")
        user = User.objects.filter(username="jordi").first()
        thesis = Thesis.objects.create(
            name='Test Thesis',
            description='',
            author_id=user.pk,
            last_ip="127.0.0.1",
            url="https://test.com",
            content=file
        )
