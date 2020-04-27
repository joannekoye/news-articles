import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_article = Article('BBC News', 'Judge sympathises with man who stabbed protesters', 'The judge who jailed the man for the attack at an anti-government protest said he was a victim.', 'http://www.bbc.co.uk/news/world-asia-china-52426377', '2020-04-25T14:49:51Z', 'Hong Kong tour guide jailed for 45 months for stabbing three people during last year\'s anti-government protests ha…',)

    
    def test_instance(self):
        '''
        Test to check if new_article instance exists
        '''
        self.assertTrue(isinstance(self.new_article, Article))

