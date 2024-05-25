import random

def main():
    while True:
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

        # take the input from user
        choice = input("Enter your choice: ")

        # looping until user enters a valid input
        while choice not in ['1', '2', '3']:
            choice = input('Enter a valid choice please ☺ (1, 2, or 3): ')

        # convert the valid input to an integer
        choice = int(choice)

        # initialize value of choice_name variable
        # corresponding to the choice value
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissors'

        # print user choice
        print('User choice is:', choice_name)
        print("Now it\'s the Computer\'s Turn....")

        # Computer chooses randomly any number among 1, 2, and 3 using randint method of random module
        comp_choice = random.randint(1, 3)

        # initialize value of comp_choice_name variable corresponding to the choice value
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'

        print("Computer choice is:", comp_choice_name)
        print(choice_name, 'Vs', comp_choice_name)

        # check if it's a draw
        if choice == comp_choice:
            print("It's a Draw")
            result = "DRAW"
        else:
            # conditions for winning
            if (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
                print(f'{comp_choice_name} wins =>')
                result = comp_choice_name
            else:
                print(f'{choice_name} wins =>')
                result = choice_name

        # Print whether user wins, computer wins, or if it's a draw
        if result == 'DRAW':
            print("<== It's a tie ==>")
        elif result == choice_name:
            print("<== User wins ==>")
        else:
            print("<== Computer wins ==>")

        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != 'y':
            break

    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    main()
