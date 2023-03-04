import os
from google.cloud import translate_v2
import re


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'googlekey.json'
pattern1 = r'\s*>([^<>]*)<'  # r'\s*[^>]*>(.*?)<\/(\w+)>'
pattern2 = r'\s*([a-zA-Z-]+)\s*:\s*([^;]+)\s*;'
pattern3 = r'(\S+)\s*=\s*["\']?((?:.(?!["\']?\s+(?:\S+)=|[>"\']))+.)["\']?'
with open('test.html', 'r+') as file:
    client = translate_v2.Client()
    with open('index.html', 'w+') as htmlfile:
        while (line := file.readline()):
            if (re.search(pattern1, line) and not re.search(pattern2, line) and len(line) < 30000):
                text = re.search(pattern1, line).group(1)
                translated_text = client.translate(text, target_language='es')
                new_html_string = line.replace(text, translated_text["translatedText"])
                print('--------------------------------')
                print('--------------------------------')
                print('--------------------------------')
                print("Line => " + line)
                print('--------------------------------')
                print("Text => " + text)
                print('--------------------------------')
                print("New String => " + new_html_string)
                print('--------------------------------')
                print('--------------------------------')
                print('--------------------------------')
                htmlfile.write(new_html_string)
            else:
                htmlfile.write(line)
        htmlfile.close()
    file.close()