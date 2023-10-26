# Simulation of a racketball game

from random import *

def main():
    printIntro()
    probA, probB, n = getInputs() # Get inputs will create probA, probB, n and these will need to be passed to the next functon therefore they need to be somewhere in the main function
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
    

def printIntro():
    print("This program simulates a game of racketball between two people")
    print("called 'A' and 'B'. The abilities of each player is indicated")
    print("by a probability (a number between 0 and 1) that the player wins")
    print("a point when serving. Player A always has the first serve.")

def getInputs():
    # Returns he three simulation parameters
    a = float(input("What is the probabiliy player A wins a serve?: "))
    b = float(input("What is the probabiliy player B wins a serve?: "))
    n = int(input("How many games would you like to simulate?: "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racketball between players whose abilities are represented by the pobability of
    # winning a serve. Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game
    # abilities are represented by probability of winning a serve
    # Returns final scores of one game for A and B
    serving = "A"
    scoreA = scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA +=1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racketball games
    # Returns true if the game is over and false otherwise
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player
    n = winsA + winsB
    print("\nGames Simulated", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    # print("Wins A = ", winsA)
    # print("Wins B = ", winsB)
    

main()