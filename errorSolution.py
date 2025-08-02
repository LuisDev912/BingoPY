"""
This is a python script (obviously) for practice the
error in the main code 'Main.py'.
"""


#the code below is the same as the one in Main.py, but I'll use this to fix the bug
#the bug is that I need to replace the number with an "X" in the player
from random import randint as rd
import time as t

repeatedNumbers = []


def createPlayerCarton():
    Carton = []
    
    while len(Carton) < 6:
        num = rd(1, 100)
        if num not in Carton:
            Carton.append(num)
    return Carton


playerCarton = createPlayerCarton()

while len(repeatedNumbers) < 100:
    Rnumber = rd(1, 100)
    # playerCarton() 
    # I realised that I don't need to call the function again, because the playerCarton is already created.
    print(f"{playerCarton[:3]},\n{playerCarton[3:]}")  # Display the carton in two lines

    if Rnumber not in repeatedNumbers:
        print("🎱 The next number is: ", end="", flush=True)
        t.sleep(0.75)
        print(f"☑️ {Rnumber}")
        repeatedNumbers.append(Rnumber) 

        #⚠️
        #so, basically, I'll try to fix the bug by deleting the number from the playerCarton and then adding it with an "X"
        if Rnumber in playerCarton:
            playerCarton.pop(Rnumber)
            playerCarton.append("X")
            
            print(f"💯You have a match!: {Rnumber} \n")
            t.sleep(0.90)
        #⚠️

    if len(playerCarton) == 0:
        print("You have completed your carton!💯")
        break
        


    print(f"❗all the numbers are: {sorted(repeatedNumbers)}") 
    if input("\n❓Do you want to continue? (yes/no): ").strip().lower() != "yes":
        break
    
print("thanks for playing!")
#for now, this is the base code. I'll add more features later.