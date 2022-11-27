import random
import string

password = ''
characters = string.ascii_letters + string.digits + string.punctuation
for x in range(16):

    password = password + random.choice(characters)

print(password)