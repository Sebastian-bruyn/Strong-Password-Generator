import random
import string
LengthOfPassword = 16
password = ''
characters = string.ascii_letters + string.digits + string.punctuation
for x in range(LengthOfPassword):

    password = password + random.choice(characters)

print(password)