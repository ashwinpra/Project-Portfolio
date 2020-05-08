# A simple choice-maker that I use to make not-so-important life choices :)
import random
import time

i = int(input("How many choices?"))
lis=[]
for n in range(i):
   lis.append(input("Enter your choices\n"))

finalChoice=random.choice(lis)

print("I choose....")
time.sleep(3)
print(finalChoice+" !")
