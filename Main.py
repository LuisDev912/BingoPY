from random import randint as rd
import time as t

repeated_numbers = []


# The idea is that the carton will be shown to the player but with a best style on the console, like this:
# --------
# [1,2,3
# ,4,5,6]
# --------


def create_player_carton():
    carton = []
    
    while len(carton) < 6:
        num = rd(1, 100)
        if num not in carton:
            carton.append(num)
    return carton



def game():
    player_carton = create_player_carton()
    
    while len(repeated_numbers) < 100:
        random_number = rd(1, 100)
        # player_carton() 
        # I realised that I don't need to call the function again, because the player_carton is already created.
        print(f"{player_carton[:3]},\n{player_carton[3:]}")  # Display the carton in two lines

        if random_number not in repeated_numbers:
            print("🎱 The next number is: ", end="", flush=True)
            t.sleep(0.75)
            print(f"☑️ {random_number}")
            repeated_numbers.append(random_number) 

            if random_number in player_carton:
                player_carton = [x if x != random_number else "X" for x in player_carton] #I used a list comprehension to replace the number with "X"
                print(f"💯You have a match!: {random_number} \n")
                t.sleep(0.90)

        if len(player_carton) == 0:
            print("You have completed your carton!💯")
            break

        print(f"❗all the numbers are: {sorted(repeated_numbers)}") 
        if input("\n❓Do you want to continue? (yes/no): ").strip().lower() != "yes":
            break

print("thanks for playing!")

if __name__ == "__main__":
    game()