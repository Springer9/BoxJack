#version3.2
#jackBox

__author__ = "Ethan Springob"

import time
import math
import random

promptTest = "Why is your mom so fat"

prompts = [
    "Why is your mom so fat?",
    "Who's the first person you call when you wake up with a cold",
    "Who's the most likely to cry about getting a B on a test",
    "testprompt3",
    "testprompt4",
    "testprompt5",
    "testprompt6",
    "testprompt7"
]

first = "test"
playerList = []
playerResponse = []
playerScore = []
gameActive = True

rounds = 3
responseTimeLimit = 30
pointIncrement = 10
currentRound = 0

def randomizePrompts():
    randNum = random.randint(0,len(prompts)-1)
    print("randNum =",randNum)
    #testtheprompt = prompts(randNum)
    return randNum

def mathFunctions():
    print("Floor division: 7 // 2 =",7//2)
    #floor divison
    print("Exponents: 8 to the power of 2, or 8 ** 2 =",8**2)
    #exponent
    print("Addition: 7 + 2 =",7+2)
    #addition
    print("Subtraction: 15 - 8 =",15-8)
    #subtraction
    print("Multiplication: 3 * 5 =",3*5)
    #multiplication
    print("Division: 15 / 3 =",15/3)
    #division



def errorMessage():
    print("invalid\n","Sending you back",sep = "")

def menuPrompt():
    startQ = input("Press Enter to Start")
    if startQ == "":
        playerCount()
    else:
        errorMessage()
        menuPrompt()

playerCount = 0
def playerCount():
    print("Game Starting")
    playerCount = int(input("How many Players? "))
    if playerCount > 1 and playerCount < 10:
        #firstLoop()
        for player in range(playerCount):
            playerList.append(player + 1)
            playerScore.append(0)
        #for playerCount do
        tutorial()
    else:
        print("Invalid Player Count")
        errorMessage()
        playerCount()


def tutorial():
    print("Welcome to version 3")
    time.sleep(2)
    print("in this game, everyone will be given the same prompt")
    time.sleep(2)
    print("your goal will be to get the most votes on your response.")
    time.sleep(2)
    print("You will be given a certain amount of points depending on how many votes.")
    mainLoop()

def endGame():
    print("Congratulations, Player",first+1,", you win with a total of",playerScore[first],"points")

def promptPlayer(player):
    print("Player",player+1,"is up.")
    response = input("Response here: ")
    playerResponse.insert(player,response)

def mainLoop():
    while gameActive:
        numTest = randomizePrompts()
        print(prompts[numTest])
        del(prompts[numTest])
        for player in range(len(playerList)):
            time.sleep(1)
            promptPlayer(player)

        votingLoop()
    endGame() #when gameActive == false, calls the endGame function

def setFirstPlace():
    global first
    for i in range(len(playerList)):
        if first == "test":
            first = i
        elif playerScore[i] > playerScore[first]:
            first = i
        elif playerScore[i] == playerScore[first]:
            first = i

def votingLoop():
    global currentRound
    global gameActive
    print("Vote for your favorite response by typing the corresponding number to the list")
    print(playerResponse)
    playerResponse.clear()
    for i in range(len(playerList)):
        print("Player", i+1, "is up")
        vote = int(input("Response: ")) - 1
        playerScore[vote] += pointIncrement
    setFirstPlace()
    print("The standings are shown below")
    print(playerScore)
    time.sleep(2)
    if first == "Tie":
        print("There is a tie!")
    else:
        print("Player ", first+1, " is in the lead!")
    currentRound = currentRound + 1
    print("current round =",currentRound)
    if currentRound >= rounds and first != "Tie":
        gameActive = False
    elif first == "Tie":
        print("There is a tie, the game continues until a winner is decided")

    mainLoop()


#Create Player Table
#For every Player repeat the following
def firstLoop():
    print("Here is the first prompt")
    time.sleep(2)
    print(promptTest)
    time.sleep(2)
    print("Player 1, you're up first")
    playerResponse = input("Response here...")
    print("player 1 said " + playerResponse)

menuPrompt()

      
