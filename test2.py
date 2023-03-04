import re

html_string = '<h1>Hello, world!</h1>'
new_text = 'Hola, mundo!'
text = re.search(r'>([^<>]*)<', html_string).group(1)
new_html_string = html_string.replace(text, new_text)
print(new_html_string)