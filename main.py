import random
print("rock,paper,scissors,the game")
print("-----------------------------")

# print the instructions for the user to see:
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")


while True:
    user_choise = input("please choose '1' for ROCK , '2' for PAPER , '3' for SCISSORS  \n ")
    pc_choise = random.choice(['1', '2', '3'])
    if user_choise == pc_choise:
        print("its a tie")
    elif user_choise == '1':
        if pc_choise == '3':
            print("you picked ROCK , computer picked SCISSORS you win (:")
        else:
            print("you picked ROCK ,computer picked PAPER you lose ):")
    elif user_choise == '2':
        if pc_choise == '1':
            print("you picked PAPER , computer picked ROCK you win (:")
        else:
            print("you picked PAPER ,computer picked SCISSORS you lose ):")
    elif user_choise == '3':
        if pc_choise == '2':
            print("you picked SCISSORS , computer picked PAPER you win (:")
        else:
            print("you picked SCISSORS  ,computer picked ROCK you lose ):")
    play = input("you want to play again ? y/n \n")
    if play == 'n':
        break














