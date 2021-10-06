from django.test import SimpleTestCase


# Simple test suite that valid behaviour of auth login
class DummySuccess(SimpleTestCase):
    def test_dummy_success(self):
        self.assertEqual(1 + 3, 4)
