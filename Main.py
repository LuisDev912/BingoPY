from random import randint as rd
import time as t

repeatedNumbers = []
carton = []

def createPlayerCarton():

    for i in range(6):
        carton.append(rd(1, 100))
    return f"Your carton is: {carton}"

while len(repeatedNumbers) < 100:
    Rnumber = rd(1, 100)
    if Rnumber not in repeatedNumbers:
        print(Rnumber)
        t.sleep(0.75)  
        repeatedNumbers.append(Rnumber) 
    else:
        continue
    
    print(f"all the numbers are: {sorted(repeatedNumbers)}") 
    if input("Do you want to continue? (yes/no): ").strip().lower() != "yes":
        break
    
print("thanks for playing!")
#for now, this is the base code. I'll add more features later.