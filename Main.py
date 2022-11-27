import random
import string


#Varibles
LengthOfPassword = 16
password = ''

#Generation
characters = string.ascii_letters + string.digits + string.punctuation
for x in range(LengthOfPassword):

    password = password + random.choice(characters)

#Output
print(password)