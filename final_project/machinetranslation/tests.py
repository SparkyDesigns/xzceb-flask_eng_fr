import unittest
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from translator import englishToFrench
from translator import frenchToEnglish

class TestfrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    def test_englishToFrench(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
