import string
import random
import sys

def id_generator(size=8, items=string.ascii_lowercase + string.digits):
     return ''.join(random.choice(items) for _ in range(size))

id_generator()
'G5G74W'
id_generator(3, "6793YUIO")
