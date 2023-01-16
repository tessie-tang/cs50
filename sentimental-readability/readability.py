import string
import re
from cs50 import get_string

text = get_string("Text: ")

letters = len(re.findall('[a-zA-Z]', text))
words = len(text.split())
sentences = len(re.findall(r'[.!?]+', text))

words_per_100 = words / 100
l = letters / words_per_100
s = sentences / words_per_100
index = round(0.0588 * l - 0.296 * s - 15.8)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade " + str(index))
