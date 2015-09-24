"""
Kya Miller
LING 539 Assignment 1
Q3A - Calculates the entropy from the sum of the rolls of two 4-sided dice. Both dice are fairly weighted.
I wasn't sure if the problem wanted the separate entropies of each dice added together, or the entropy of the probabilities
of getting each possible sum from the two dice rolls (2-8), so I did both.
"""

from __future__ import division
import math


def calculateEntropy(listOfProbabilities):
    sum = 0
    for probability in listOfProbabilities:
        sum += probability * math.log(probability, 2)

    return -sum


dice1Entropy = calculateEntropy([0.25, 0.25, 0.25, 0.25])
dice2Entropy = calculateEntropy([0.25, 0.25, 0.25, 0.25])
sumEntropy = dice1Entropy + dice2Entropy
print(sumEntropy)

totalSumsEntropy = calculateEntropy([1 / 16, 2 / 16, 3 / 16, 4 / 16, 3 / 16, 2 / 16, 1 / 16])
print(totalSumsEntropy)
