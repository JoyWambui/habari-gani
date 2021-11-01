import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    """Test Class to test the behaviour of the Article class"""

    def setUp(self):
        """Set up method that will run before every Test"""
        self.new_article = Article("jack", "fuel prices continue to soar","Fuel prices will continue on an upward trajectory",
                                   "https://abcnews.go.com/International/wireStory/barclays-ceo-steps-epstein-report-uk-regulators-80898706",
                                   "https://live-production.wcms.abc-cdn.net.au/7e4effe5d666816e6a177165d71cebf3?impolicy=wcms_crop_resize&cropH=1701&cropW=3024&xPos=0&yPos=763&width=862&height=485",
                                   "2021-11-01T06:08:56Z")

    def test_instance(self):
        """Test that confirms an article object is an instance of the Article class"""
        self.assertTrue(isinstance(self.new_article,Article))
        
    def test_correct_instantiation(self):
        """Test that confirms an article object instantiates with the right attributes."""
        self.assertEqual(self.new_article.author,"jack")
        self.assertEqual(self.new_article.title,"fuel prices continue to soar")
        self.assertEqual(self.new_article.description,"Fuel prices will continue on an upward trajectory")
        self.assertEqual(self.new_article.url,"https://abcnews.go.com/International/wireStory/barclays-ceo-steps-epstein-report-uk-regulators-80898706")
        self.assertEqual(self.new_article.image_url,"https://live-production.wcms.abc-cdn.net.au/7e4effe5d666816e6a177165d71cebf3?impolicy=wcms_crop_resize&cropH=1701&cropW=3024&xPos=0&yPos=763&width=862&height=485")
        self.assertEqual(self.new_article.published,"2021-11-01T06:08:56Z")

if __name__ == '__main__':
    unittest.main()