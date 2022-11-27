import random
import string
lengtgOfPassword = 16
password = ''
characters = string.ascii_letters + string.digits + string.punctuation
for x in range(lengtgOfPassword):

    password = password + random.choice(characters)

print(password)