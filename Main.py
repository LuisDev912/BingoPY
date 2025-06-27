from random import randint as rd
import time as t

repeatedNumbers = []

def createPlayerCarton():
    newCarton = []
    
    while len(newCarton) < 6:
        num = rd(1, 100)
        if num not in newCarton:
            newCarton.append(num)
    return newCarton

newCarton = createPlayerCarton()

while len(repeatedNumbers) < 100:
    Rnumber = rd(1, 100)
    print(newCarton)

    if Rnumber not in repeatedNumbers:
        print(f"☑️ {Rnumber}")
        t.sleep(0.75)  
        repeatedNumbers.append(Rnumber) 

        if Rnumber in newCarton:
            print(f"💯You have a match!: {Rnumber} \n")
            newCarton.remove(Rnumber)
            t.sleep(0.90)

    if len(newCarton) == 0:
        print("You have completed your carton!💯")
        break
        


    print(f"❗all the numbers are: {sorted(repeatedNumbers)}") 
    if input("\n❓Do you want to continue? (yes/no): ").strip().lower() != "yes":
        break
    
print("thanks for playing!")
#for now, this is the base code. I'll add more features later.