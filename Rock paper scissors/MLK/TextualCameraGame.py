import Score
import Camera
import LoadGame
import os
import time
import random

Yes = ["1", "oui", "yes", "o", "y"]
No = ["2", "non", "no", "n"]
Moves = ["SCISSORS", "PAPER", "ROCK"]

def MainMenu():
    print("\n----- Menu principal -----\n")
    Score.ShowScore()
    WantToPlay()

def WantToPlay():
    choice = input("\nVoulez-vous jouer ?\n1 - Oui\n2 - Non\n")
    if (choice in Yes):
        Play()
    elif (choice in No):
        os._exit
    else:
        print("Erreur, choix incorrect")
        WantToPlay()

def Play():
    global myproject
    print("\nPréparez-vous, photo prise dans 3 secondes...\n")
    time.sleep(3)
    #Camera.TakePicture()
    move = myproject.prediction(Camera.GetFileName())
    userMove = ConvertUserMove(move)
    computerMove = GetComputerMove()
    Score.GetWinner(userMove, computerMove)
    Score.ShowScore()
    WantToPlay()

def ConvertUserMove(move):
    return move["class_name"]

def GetComputerMove():
    choice = random.randint(1, 3)
    return Moves[choice-1]

# Program starts here :

print(os.getcwd())
myproject = LoadGame.LoadProject()
MainMenu()