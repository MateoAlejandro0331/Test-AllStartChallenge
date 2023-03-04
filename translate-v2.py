import os
from google.cloud import translate_v2
from re import search


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'googlekey.json'
pattern1 = r'>([^<>]*)<'
pattern2 = r'\s*([a-zA-Z-]+)\s*:\s*([^;]+)\s*;'
i = 0
with open('test.html', 'r+') as file:
    client = translate_v2.Client()
    with open('new.html', 'w+') as htmlfile:
        while (line := file.readline()):
            if (search(pattern1, line) and not search(pattern2, line) and len(line) < 30000):
                translate = line.split(">")
                translated_text = client.translate(translate[1], target_language='es')
                finalString = translate[0] + '>' + \
                translated_text["translatedText"] + translate[2] + '> \n'
                htmlfile.write(finalString)
            else:
                htmlfile.write(line)
