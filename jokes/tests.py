from django.test import TestCase

# Create your tests here.

class URLTests(TestCase):
    def test_testcornyoutput(self):
        responsefromfxn = self.client.get("/api/jokes/corny")
        self.assertEqual(responsefromfxn.status_code,200)
