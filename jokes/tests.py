from django.test import TestCase
from django.urls import reverse
from rest_framework import status
import json
# Create your tests here.

class URLTests(TestCase):
    cornylink = reverse('corny')
    def test_testcornystatus(self):
        responsefromfxn = self.client.get(self.cornylink)
        self.assertEqual(responsefromfxn.status_code,200)


    def test_testcornyoutputcontent(self):
        responsefromfxn = self.client.get(self.cornylink)
        self.assertEqual(responsefromfxn.status_code,status.HTTP_200_OK)
        self.assertEqual(json.loads(responsefromfxn.content),'hello')