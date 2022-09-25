from hashlib import new
from unicodedata import digit


char = str(input('Write a two digit number'))

digit1 = char[0]

digit2 = char[1]

print(int(digit1) + int(digit2))