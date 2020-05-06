import random
s="abcdefghijklmnopqrstuvwxyz@#&/1234567890"
passwordlen=8
password="".join(random.sample(s,passwordlen))
print(password)