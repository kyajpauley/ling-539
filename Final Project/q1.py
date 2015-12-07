"""
Kya Miller
LING 539 Assignment 6 - Final Project
Q1 -
"""
import nltk
import re


def getGoldLabels():
    goldDataFileIn = open('goldData/index.txt', 'r')
    goldDataLines = goldDataFileIn.readlines()
    goldDataFileIn.close()

    goldDataLabels = []
    for line in goldDataLines[:3000]:
        splitLine = line.split(' ', 1)
        label = splitLine[0].lower()
        goldDataLabels.append(label)

    trainingGoldLabels = goldDataLabels[:1000]
    developmentGoldLabels = goldDataLabels[1000:2000]
    testingGoldLabels = goldDataLabels[2000:3000]

    return trainingGoldLabels, developmentGoldLabels, testingGoldLabels


def getEmailText(emailLines):
    emailText = ''
    done = False
    while not done:
        for i in range(len(emailLines)):
            if emailLines[i].startswith('Lines:'):
                emailText = ' '.join(emailLines[i + 1:])
                done = True
    return emailText


def getTrainingData(trainingLabels):
    trainingData = []
    for i in range(1000):
        trainingEmailFileIn = open('trainingData/inmail.%s' % (i + 1), 'r')
        trainingEmailLines = trainingEmailFileIn.readlines()
        trainingEmailFileIn.close()
        trainingData.append([getEmailText(trainingEmailLines), trainingLabels[i]])
    return trainingData


def getDevelopmentData(developmentLabels):
    developmentData = []
    startNumber = 1000
    for i in range(1000):
        developmentEmailFileIn = open('developmentData/inmail.%s' % (startNumber + i + 1), 'r')
        developmentEmailLines = developmentEmailFileIn.readlines()
        developmentEmailFileIn.close()
        developmentData.append([getEmailText(developmentEmailLines), developmentLabels[i]])
    return developmentData


def getTestingData(testingLabels):
    testingData = []
    startNumber = 2000
    for i in range(1000):
        testingEmailFileIn = open('testingData/inmail.%s' % (startNumber + i + 1), 'r')
        testingEmailLines = testingEmailFileIn.readlines()
        testingEmailFileIn.close()
        testingData.append([getEmailText(testingEmailLines), testingLabels[i]])
    return testingData


def doesHTMLExist(emailText):
    if re.search('<HTML>', emailText):
        return True
    else:
        return False


def areThereReallyLongSequences(emailText):
    # checks for emails that have super long sequences of jumbled text. Simply checks for the existence of 'words' with
    # a length longer than 50 characters
    words = ' '.split(emailText)
    tooLong = False
    for word in words:
        if len(word) > 50:
            if 'http' not in word:
                tooLong = True
    return tooLong


def checkForErectileDysfunction(emailText):
    # check for words involving erectile dysfunction
    erectileDysfunctionMessage = False
    definitelyEDWords = ['viagra', 'cialis', 'levitra', 'v i a g r a', 'c i a l i s', 'l e v i t r a']
    wordsRelatingToED = ['manhood', 'small', 'area', 'perform', 'inches', 'pill', 'length', 'big', 'libido', 'orgasm',
                         'fix', 'drug']
    definiteCounter = 0
    maybeCounter = 0
    for word in definitelyEDWords:
        if re.findall(word, emailText.lower()):
            definiteCounter += len(re.findall(word, emailText.lower()))
    for word in wordsRelatingToED:
        if re.findall(word, emailText.lower()):
            maybeCounter += len(re.findall(word, emailText.lower()))

    if definiteCounter >= 2:
        erectileDysfunctionMessage = True
    if maybeCounter >= 3:
        erectileDysfunctionMessage = True

    return erectileDysfunctionMessage


def checkForHealth(emailText):
    # check for words involving weight loss
    weightLossOrHealthMessage = False
    weightLossOrHealthWords = ['fat', 'fit', 'weight', 'food', 'loss', 'growing', 'pound', 'kilo', 'health', 'eat',
                               'ate', 'overweight', 'slender', 'energy', 'lose', 'pill', 'anti-aging', 'youth',
                               'prescription', 'drug', 'quality', 'stimulate', 'hormone', 'appetite', 'natural',
                               'losing', 'substance']
    healthCounter = 0
    for word in weightLossOrHealthWords:
        if re.findall(word, emailText.lower()):
            healthCounter += len(re.findall(word, emailText.lower()))

    if healthCounter >= 3:
        weightLossOrHealthMessage = True
    return weightLossOrHealthMessage


def checkForMoney(emailText):
    # check for words involving money or ordering things or money scams
    moneyMessage = False
    moneyWords = ['money', 'order', 'buy', 'dollar', 'today', 'transaction', 'commission', 'earn', 'cash', 'payment',
                  'bank', 'receipt', 'work', 'work from home', 'capital', 'pay', 'ship', 'cheap', 'discount', 'price',
                  'delivery', 'refinance', 'property', 'finance']
    moneyCounter = 0
    for word in moneyWords:
        if re.findall(word, emailText.lower()):
            moneyCounter += len(re.findall(word, emailText.lower()))

    if moneyCounter >= 2:
        moneyMessage = True
    return moneyMessage


def createFeatureSet(emailText):
    features = {}
    features['HTML'] = doesHTMLExist(emailText)
    features['tooLongSequences'] = areThereReallyLongSequences(emailText)
    features['isAboutED'] = checkForErectileDysfunction(emailText)
    features['isAboutHealth'] = checkForHealth(emailText)
    features['isAboutMoney'] = checkForMoney(emailText)
    return features


trainingLabels, developmentLabels, testingLabels = getGoldLabels()
trainingData = getTrainingData(trainingLabels)
trainingData = [[createFeatureSet(emailText), label] for [emailText, label] in trainingData]
developmentData = getDevelopmentData(developmentLabels)
developmentData = [[createFeatureSet(emailText), label] for [emailText, label] in developmentData]
testingData = getTestingData(testingLabels)
testingData = [[createFeatureSet(emailText), label] for [emailText, label] in testingData]
