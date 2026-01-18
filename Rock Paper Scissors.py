import random

while True:
    computer = random.randint(1, 3)
    player = input(" 1: Rock \n 2: Paper \n 3: Scissors   \n: ")
    numb = int(player)
    if numb == computer:
        print("Draw!")
        print("Would you like to play again? ")
        again = input()
        if again != "yes" and again != "y" and again != "Y" and again != "Yes":
            break
    if numb == 1 and computer == 3 or numb == 2 and computer == 1 or numb == 3 and computer == 2:
        print("You win!")
        print("Would you like to play again? ")
        again = input()
        if again != "yes" and again != "y" and again != "Y" and again != "Yes":
            break
    if numb == 1 and computer == 2 or numb == 2 and computer == 3 or numb == 3 and computer == 1:
        print("You lose!")
        print("Would you like to play again? ")
        again = input()
        if again != "yes" and again != "y" and again != "Y" and again != "Yes":
            break