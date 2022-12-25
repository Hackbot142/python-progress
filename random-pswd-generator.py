import random
import string

def generate_password(length):
  characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
  
  random.shuffle(characters)
  
  password = random.choices(characters, k=length)
  
  return ''.join(password)

print(generate_password(8)) 