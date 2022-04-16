import speech_recognition as sr
import pyttsx3
import VocalScore
import os
import random

Yes = ["oui", "yes"]
No = ["non", "no"]
Moves = ["CISEAUX", "FEUILLE", "PIERRE"]
Ciseaux = ["ciseaux", "six eau", "6 eau", "6 os", "six os", "six zoo", "6 zoo", "si zoo", "scie", "six", "si"]
Pierre = ["pierre", "pi aire", "hier", "tier"]
Feuille = ["feuille", "papier", "pas pied", "pas pieds", "pape", "pape hier", "feu", "failli"]

listener = sr.Recognizer()
engine = pyttsx3.init()

def MainMenu():
    engine.say("Bienvenue dans le jeu pierre feuille ciseaux en version vocale")
    engine.runAndWait()
    WantToPlay()

def WantToPlay():
    engine.say("Voulez-vous faire une partie ?")
    engine.runAndWait()
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="fr-FR")
            if (command in Yes):
                Play()
            elif (command in No):
                os._exit
            else:
                engine.say("Erreur, choix incorrect")
                engine.runAndWait()
                WantToPlay()
    except sr.UnknownValueError:
        engine.say("Erreur, choix incorrect")
        engine.runAndWait()
        WantToPlay()

def Play():
    userMove = ""
    engine.say("Que voulez-vous jouer ? Pierre, feuille ou ciseaux ?")
    engine.runAndWait()
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="fr-FR")
            if (command.lower() in Ciseaux):
                userMove = Moves[0]
            elif (command.lower() in Feuille):
                userMove = Moves[1]
            elif (command.lower() in Pierre):
                userMove = Moves[2]
            else:
                engine.say("Erreur, choix incorrect")
                engine.runAndWait()
                Play()
            computerMove = GetComputerMove()
            VocalScore.GetWinner(userMove, computerMove)
            VocalScore.ShowScore()
            WantToPlay()
    except sr.UnknownValueError:
        engine.say("Erreur, choix incorrect")
        engine.runAndWait()
        Play()

def GetComputerMove():
    choice = random.randint(1, 3)
    return Moves[choice-1]

# Program starts here :

MainMenu()