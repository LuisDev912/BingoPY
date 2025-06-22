import random as rd
import time as t

repeatedNumbers = []

while len(repeatedNumbers) < 100:
    Rnumber = rd.randint(1, 100)
    if Rnumber not in repeatedNumbers:
        print(Rnumber)
        t.sleep(2.5)  # Sleep for a while, it's like a delay
        repeatedNumbers.append(Rnumber) 
    else:
        continue
    
    print(f"all the numbers are: {sorted(repeatedNumbers)}") 
    if input("Do you want to continue? (yes/no): ").strip().lower() != "yes":
        break
    
print("BINGO!, thanks for playing!")
#for now, this is the base code. I'll add more features later.