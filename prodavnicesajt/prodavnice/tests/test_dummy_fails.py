from django.test import SimpleTestCase


# Dummy test case that fails
class KaseLoginTests(SimpleTestCase):
    def test_dummy_fails(self):
        self.assertEqual(2 + 2, 5)

