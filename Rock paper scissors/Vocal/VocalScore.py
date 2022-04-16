import pyttsx3

userScore = 0
computerScore = 0
engine = pyttsx3.init()

def GetWinner(userMove, computerMove):
    engine.say("Vous avez joué : {0}L'ordinateur à joué : {1}" .format(userMove, computerMove))
    engine.runAndWait()
    if (userMove.upper() == computerMove.upper()):
        Draw()
    elif (userMove.upper() == "CISEAUX"):
        if(computerMove.upper() == "PIERRE"):
            ComputerWins()
        else:
            UserWins()
    elif (userMove.upper() == "PIERRE"):
        if(computerMove.upper() == "FEUILLE"):
            ComputerWins()
        else:
            UserWins()
    elif (userMove.upper() == "FEUILLE"):
        if(computerMove.upper() == "PIERRE"):
            UserWins()
        else:
            ComputerWins()

def Draw():
    engine.say("C'est une égalité !")
    engine.runAndWait()

def ShowScore():
    engine.say("Vous avez {0} points".format(userScore))
    engine.runAndWait()
    engine.say("L'ordinateur à {0} points".format(computerScore))
    engine.runAndWait()

def ComputerWins():
    engine.say("L'ordinateur gagne !")
    engine.runAndWait()
    global computerScore
    computerScore += 1

def UserWins():
    engine.say("Vous gagnez !")
    engine.runAndWait()
    global userScore
    userScore += 1