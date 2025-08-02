from random import randint as rd
import time as t

repeatedNumbers = []

"""
The idea is that the carton will be shown to the player but with a best style on the console, like this:
--------
[1,2,3
,4,5,6]
--------
"""

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

        if Rnumber in playerCarton:
            playerCarton = [x if x != Rnumber else "X" for x in playerCarton] #I used a list comprehension to replace the number with "X"
            print(f"💯You have a match!: {Rnumber} \n")
            t.sleep(0.90)

    if len(playerCarton) == 0:
        print("You have completed your carton!💯")
        break
        


    print(f"❗all the numbers are: {sorted(repeatedNumbers)}") 
    if input("\n❓Do you want to continue? (yes/no): ").strip().lower() != "yes":
        break
    
print("thanks for playing!")
#for now, this is the base code. I'll add more features later.