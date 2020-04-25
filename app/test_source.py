import unittest
from models import source

Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test behavior or source class
    '''

    def setUp(self):
        '''
        Setup method that will run before evry test
        '''
        self.new_source = Source('bbc-news', 'BBC News', 'Use BBC News for up-to-the-minute news, breaking news, video, audio and feature stories. BBC News provides trusted World and UK news as well as local and regional perspectives. Also entertainment, business, science, technology and health news.', 'http://www.bbc.co.uk/news', 'general', 'en', 'gb')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))


if __name__ == '__main__':
    unittest.main()