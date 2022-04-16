userScore = 0
computerScore = 0

def GetWinner(userMove, computerMove):
    print("Vous avez joué : {0}\nL'ordinateur à joué : {1}\n" .format(userMove.capitalize(), computerMove.capitalize()))
    if (userMove.upper() == computerMove.upper()):
        Draw()
    elif (userMove.upper() == "SCISSORS"):
        if(computerMove.upper() == "ROCK"):
            ComputerWins()
        else:
            UserWins()
    elif (userMove.upper() == "ROCK"):
        if(computerMove.upper() == "PAPER"):
            ComputerWins()
        else:
            UserWins()
    elif (userMove.upper() == "PAPER"):
        if(computerMove.upper() == "ROCK"):
            UserWins()
        else:
            ComputerWins()

def Draw():
    print("C'est une égalité !")

def ShowScore():
    print("\nVotre score : {0}".format(userScore))
    print("Score de l'ordinateur : {0}\n".format(computerScore))

def ComputerWins():
    print("L'ordinateur gagne !")
    global computerScore
    computerScore += 1

def UserWins():
    print("Vous gagnez !")
    global userScore
    userScore += 1