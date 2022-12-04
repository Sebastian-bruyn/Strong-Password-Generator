import argparse
import random
import string

#make easier to adjust length
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length",required=True, type=int)
args = parser.parse_args()


    
password = ''
LengthOfPassword = args.length

#Generation
characters = string.ascii_letters + string.digits + string.punctuation
for x in range(LengthOfPassword):
    password = password + random.choice(characters)

#Output
print(password)