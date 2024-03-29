__author__ = 'Kya'
# September 8, 2015

from random import randint

class MonteHall(object):
    def __init__(self, numIterations):
        self.GoatDoor = 0
        self.WinningDoor = 1
        self.OpenDoor = 2

        self.numIterations = numIterations

        finalScoreNormal = self.doExperimentNormal()
        finalScoreSwitch = self.doExperimentSwitch()

        print("Final Score after %s iterations with no switching: %s" % (self.numIterations, finalScoreNormal))

        print("Final Score after %s iterations with switching: %s" % (self.numIterations, finalScoreSwitch))

    def setWinningDoor(self):
        doorValues = [self.GoatDoor] * 3
        randomWinningDoor = randint(0,2)
        doorValues[randomWinningDoor] = self.WinningDoor
        return doorValues

    def chooseDoor(self):
        return randint(0,2)

    def openNonWinningDoor(self, doorValues, chosenDoor):
        randomDoor = randint(0, 2)
        done = False
        while not done:
            if randomDoor != chosenDoor and doorValues[randomDoor] == self.GoatDoor:
                done = True
            else:
                randomDoor = randint(0, 2)

        return randomDoor

    def doSwitch(self, chosenDoor, openedDoor):
        available = True
        unavailable = False
        doors = [available] * 3
        doors[chosenDoor] = unavailable
        doors[openedDoor] = unavailable

        for i in range(0, 3):
            if doors[i]:
                return i

    def isCorrect(self, doorValues, chosenDoor):
        if doorValues[chosenDoor] == self.WinningDoor:
            return True
        else:
            return False

    def doExperimentNormal(self):
        numCorrect = 0

        for i in range(0, self.numIterations):
            doorValues = self.setWinningDoor()
            chosenDoor = self.chooseDoor()

            if self.isCorrect(doorValues, chosenDoor):
                numCorrect += 1

            '''
            if self.isCorrect(doorValues, chosenDoor):
                print("Win!")
            else:
                print("Lose!")
            '''

        finalScore = (float(numCorrect) / float(self.numIterations)) * 100

        return finalScore


    def doExperimentSwitch(self):
        numCorrect = 0

        for i in range(0, self.numIterations):
            doorValues = self.setWinningDoor()
            chosenDoor = self.chooseDoor()
            openDoor = self.openNonWinningDoor(doorValues, chosenDoor)
            switchDoor = self.doSwitch(chosenDoor, openDoor)

            if self.isCorrect(doorValues, switchDoor):
                numCorrect += 1

            '''
            if self.isCorrect(doorValues, chosenDoor):
                print("Win!")
            else:
                print("Lose!")
            '''

        finalScore = (float(numCorrect) / float(self.numIterations)) * 100

        return finalScore

MonteHall(10000)

