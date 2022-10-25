import unittest
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

class TestfrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual('Hello', 'Bonjour')
    def test_englishToFrench(self):
        self.assertEqual('Bonjour', 'Hello')

unittest.main()
