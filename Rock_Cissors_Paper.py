import random

def choose_rsp():
    r = random.randint(0,2)

    if r == 0:
        return "rock"
    if r == 1:
        return "scissors"
    else:
        return "paper"


def rsp(player1, player2):
    """
    input: player1 and player2 --> 'rock', 'paper', 'scissors'
    output: 'player1 won!', 'player2 won!', 'It's a tie'
    """
    #it's a tie
    if player1 == player2:
        print("It's a tie!")

    #player 1 = rock
    elif player1 == "rock" and player2 == "paper":
        print("Player 2 won!")
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 won")

    #player 1 = paper
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 won!")
    elif player1 == "paper" and player2 == "scissors":
        print("Player 2 won!")

    #player 1 = scissors
    elif player1 == "scissors" and player2 == "rock":
        print("Player 2 won!")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 won!")

#choose input:
print("Welcome to Rock, Paper, Scissors!\n")
play = True
while play == True:    
    player1 = choose_rsp()
    player2 = choose_rsp()
    print("Player 1 chose", player1, ".")
    print("Player 2 chose", player2, ".")
    rsp(player1, player2)
    play = random.choice([True, False])
    if play == False:
        print("Thank you for playing!")

# rsp('rock', 'paper')
# rsp('rock', 'scissors')
