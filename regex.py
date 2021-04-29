import re


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

cat
bat
mat
nat
lat

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''


sentence = 'Start a sentence and then bring it to an end'

""""
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
"""

#pattern = re.compile(r'\d')
#pattern = re.compile(r'\D')
#pattern = re.compile(r'\w')
#pattern = re.compile(r'\W')
#pattern = re.compile(r'\s')
#pattern = re.compile(r'\S')

# Anchors
#pattern = re.compile(r'coreyms.com')

#pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
#pattern = re.compile(r'\d\d\d[*]\d\d\d[*]\d\d\d\d')
#pattern = re.compile(r'[9876]00[-.]\d\d\d[-.]\d\d\d\d')
#pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
#pattern = re.compile(r'[9876]\d{2}[-.]\d{3}[-.]\d{4}')
#pattern = re.compile(r'[1-5]')
#pattern = re.compile(r'[a-z]')
#pattern = re.compile(r'[a-zA-Z]')

#NEGACION DE PATTERNS
#pattern = re.compile(r'[^a-zA-Z]')
#pattern = re.compile(r'[^b]at')
#pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
#pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

#pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
#pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
#pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.(com|edu|pit)')

pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+')

with open("data.txt","r", encoding="utf-8") as f:
    content = f.read()
    matches = pattern.finditer(content)
    for match in matches:
        print(match)


#for match in matches:
#    print(match)


#pattern = re.compile('https?://(www\.)?(\w+)(\.\w+)')