print("Welcome to John's Apple Stand")
apples = input('How many apples would you like?')
if int(apples)<1 :
    print("Well, you weren't good enough for apples anyway!")
if int(apples)>10 :
    print("Sorry, we only have ten apples.")
    apples=10
for i in range(int(apples)):
    print(str(i)+" apple")
and
slotsPossible = ["bar","bar","bar","cherry","crown"]
from random import *
slot1=choice(slotsPossible)
slot2=choice(slotsPossible)
slot3=choice(slotsPossible)
print(slot1+":"+slot2+":"+slot3)

if (slot1==slot2==slot3=="cherry"):
    print("You win $100")
if (slot1==slot2==slot3=="crown"):
    print("You win $50")
if (slot1==slot2==slot3=="bar"):
    print("You win $5")
