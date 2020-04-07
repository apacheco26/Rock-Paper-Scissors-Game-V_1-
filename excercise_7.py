play_again = 0

while play_again == 0:
    print('Welcome to my rock, paper, scissors game!!\n')
    print("""
        Rules: 
        Rock beats scissors
        Scissors beats paper
        paper beats rock
        """)



    user_1 = input('Player 1: Enter choice -->')
    user_2 = input('Player 2: Enter choice -->')

    if 'rock' in user_1:
        if 'scissor' in user_2:
            print("Player 1 Wins")
            again = input('Play again: Y or N:\n')
            if 'n' in again:
                play_again += 1
        elif 'paper'in user_2:
            print("Player 2 Wins")
            again = input('Play again: Y or N:\n')
            if 'n' in again:
                play_again += 1
        elif 'rock' in user_2:
            print("Tie Game!")
            again = input('Play again: Y or N:\n')
            if 'n' in again:
                play_again += 1
        else:
            print("Error")
    elif 'scissor' in user_1:
        if 'scissors' in user_2:
            print("Tie Game!")
            again = input('Play again: Y or N:\n')
            if 'n' in again:
                play_again += 1
        elif 'paper'in user_2:
            print("Player 1 Wins")
            again = input('Play again: Y or N:\n')
            if 'n' in again:
                play_again += 1
        elif 'rock' in user_2:
            print("Player 2 Wins")
            again = input('Play again: Y or N:\n')
            if 'n' in again:
                play_again += 1
        else:
            print("Error")
    elif 'paper' in user_1:
        if 'scissor' in user_2:
            print("Player 2 Wins")
            again = input('Play again: Y or N:\n')
            if 'n' in again:
                play_again += 1
        elif 'paper'in user_2:
            print("Tie Game!")
            again = input('Play again: Y or N:\n')
            if 'n' in again:
                play_again += 1
        elif 'rock' in user_2:
            print("Player 1 wins")
            again = input('Play again: Y or N:\n')
            if 'n' in again:
                play_again += 1
        else:
            print("Error")
            print("\nTry Again")
    else:
        print("\nTry entering a valid input\n")
        