import os
from google.cloud import translate_v2

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'googlekey.json'

client = translate_v2.Client()

translate = client.translate("Hi, I love you", target_language='es')


print(translate["translatedText"])
