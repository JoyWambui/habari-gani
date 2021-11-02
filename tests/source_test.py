import unittest
from app.models import Source
class SourceTest(unittest.TestCase):
    """Test Class to test the behaviour of the Source class"""

    def setUp(self):
        """Set up method that will run before every Test"""
        self.new_source = Source("bbc", "BBC","Home of objective news","https://www.bbc.com/","General","UK")

    def test_instance(self):
        """Test that confirms a source object is an instance of the Source class"""
        self.assertTrue(isinstance(self.new_source,Source))
        
    def test_correct_instantiation(self):
        """Test that confirms a source object instantiates with the right attributes."""
        self.assertEqual(self.new_source.id,"bbc" )
        self.assertEqual(self.new_source.name,"BBC")
        self.assertEqual(self.new_source.description, "Home of objective news")
        self.assertEqual(self.new_source.url,"https://www.bbc.com/")
        self.assertEqual(self.new_source.category, "General")
        self.assertEqual(self.new_source.country, "UK")
