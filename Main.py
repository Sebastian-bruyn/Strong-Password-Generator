import random
import string
password = ''
for x in range(16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = password + random.choice(characters)

print(password)