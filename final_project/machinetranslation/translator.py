import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def english_to_french(englishtext): #function to translate english to french
    translation = language_translator.translate(text=englishtext, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(frenchtext): #function to translate french to english
    translation_new = language_translator.translate(text=frenchtext, model_id='fr-en').get_result()
    english_text = translation_new['translations'][0]['translation']
    return english_text
