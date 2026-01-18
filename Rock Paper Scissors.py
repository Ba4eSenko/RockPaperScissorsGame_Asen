import random
computer = random.randint(1,3)
while True:
    player = input(" 1: Rock \n 2: Paper \n 3: Scissors   \n: ")
    numb = int(player)
    if numb == computer:
        print("Draw!")
        print("Would you like to play again? ")
        again = input()
        if again == "yes" or again == "y" or again == "Y" or again == "Yes":
            player = input(" 1: Rock \n 2: Paper \n 3: Scissors   \n: ")
        if again == "no" or again == "n" or again == "No" or again == "NO":
            break
    if numb == 1 and computer == 3 or numb == 2 and computer == 1 or numb == 3 and computer == 2:
        print("You win!")
        print("Would you like to play again? ")
        again = input()
        if again == "yes" or again == "y" or again == "Y" or again == "Yes":
            player = input(" 1: Rock \n 2: Paper \n 3: Scissors   \n: ")
        if again == "no" or again == "n" or again == "No" or again == "NO":
            break
    if numb == 1 and computer == 2 or numb == 2 and computer == 3 or numb == 3 and computer == 1:
        print("You lose!")
        print("Would you like to play again? ")
        again = input()
        if again == "yes" or again == "y" or again == "Y" or again == "Yes":
            player = input(" 1: Rock \n 2: Paper \n 3: Scissors   \n: ")
        if again == "no" or again == "n" or again == "No" or again == "NO":
            break