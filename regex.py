import re

pattern = r'[^>]*>(.*?)<\/(\w+)>'
text = '>View all Health &amp; Medicine</span>'

match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")
    
