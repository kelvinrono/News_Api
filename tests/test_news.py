import unittest
from app.models import Articles

class NewsTest(unittest.TestCase):

    # new_news = []
    def setUp(self):

        self.new_news = Articles('testImageUrl', 'Tesla no longer accept bitcoins', '12/12/2020', 'Bitcoin no longer accepted', 'testSourceUrl')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, Articles))

    