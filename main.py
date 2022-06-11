import string
import random
import time 

wait = input('Type how many secconds you want between codes\n')
print('wait time set to %s ' % wait + 'seccond(s)')

Key_Len = 24
Link = 'https://discord.gift/'

waittime= float(wait)
Generator = (string.ascii_letters + string.digits)
Generator1 = [random.choice(Generator)for i in range(Key_Len)]
Generator2 = (''.join(Generator1)) 
output = (Link + Generator2)
count = 0

while (count < 3):
   Generator = (string.ascii_letters + string.digits)
   Generator1 = [random.choice(Generator)for i in range(Key_Len)]
   Generator2 = (''.join(Generator1))
   output = (Link + Generator2)
   print(output)
   with open('output.txt', 'a') as f:
     f.write(output + '\n')
   time.sleep(waittime)