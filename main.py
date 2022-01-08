#!/bin/env python
import math
import random
import enum
import statistics
from numpy import random
import matplotlib.pyplot as plt



NUMBER_OF_SIMULATION = 10000        # Number of times the simulation will be conducted
class Dist(enum.Enum):              # Enum class to specify the distributions 
   UNIFORM = 0
   BETA = 1


# A method that contains program animation 
def inrto():
    print("#############################################################")
    print("#                                                           #")
    print("#                       NASA Astronauts                     #")
    print("#                                                           #")
    print("#############################################################")


# A function to generate n random number with certain distribution 
def genProb(n: int, distribution: Dist, a, b) -> list:
    L = []

    # Generate 
    if distribution == Dist.BETA:
        L = random.beta(a, b, n)
    elif distribution == Dist.UNIFORM: 
        L = random.uniform(size=n)

    # Normalize
    mini = min(L)
    maxi = max(L) 
    L = [(i - mini) / (maxi - mini) for i in L]

    return L


# This method will perform the simulation and return two dictionaries
#   The first dictionary is the selected astronuts based on the overall score
#   The second dictionary is the selected astronuts based on the hardworking only
#   Each astronut is represented as a list of [Luck + HardWorking, HardWorking Value, Luck Value]
def toySim(candCount, candPassed, luckPercentage, distibutionType, a, b):
    finalDicBasedOnOverallScore = {}
    finalDicBasedOnHardWorking = {}
    firstTime = 1

    for numSim in range(0, NUMBER_OF_SIMULATION): 
    
        # Generate Random Numbers
        hardWorkingList = genProb(candCount, distibutionType, a, b)
        LuckList = genProb(candCount, distibutionType, a, b)

        # if firstTime == 1:
        #   firstTime = 0
        #   print(f"[+] The (mean, median, STD) for the hard working values: ({str(statistics.mean(LuckList))},{str(statistics.median(LuckList))}, {str(statistics.stdev(LuckList))})")
        #   plt.hist(LuckList)
        #   plt.show()

        sumDic = []
        # Scale and Add up
        for i in range(0, candCount):
            LuckList[i] = LuckList[i] * luckPercentage
            hardWorkingList[i] = hardWorkingList[i] * (1 - luckPercentage)
            sumDic.append([LuckList[i] + hardWorkingList[i], hardWorkingList[i], LuckList[i]])

        # Sort and Get the top astronauts based on the over all score 
        sortedVal = sorted(sumDic, key=lambda x: x[0])
        sortedVal.reverse()
        finalDicBasedOnOverallScore[numSim] = sortedVal[0:candPassed]
        
        # Sort and Get the top astronauts based on hard working only
        sortedVal = sorted(sumDic, key=lambda x: x[1])
        sortedVal.reverse()
        finalDicBasedOnHardWorking[numSim] = sortedVal[0:candPassed]

        # Progress ... 
        if numSim % 4 == 0:
            print("......./", end='\r')
        elif numSim % 4 == 1:
            print(".......-", end='\r')
        elif numSim % 4 == 2:
            print(".......\\", end='\r')
        elif numSim % 4 == 3:
            print(".......|", end='\r')

    return (finalDicBasedOnOverallScore, finalDicBasedOnHardWorking)


# A method to calculate max, min, mean, median, std and return them as a string 
def calcStatistics(arr):
    mean = round(statistics.mean(arr), 4)
    median = round(statistics.median(arr), 4)
    stdev = round(statistics.stdev(arr), 4)
    maxi = round(max(arr), 4)
    mini = round(min(arr), 4)

    return f"({str(mean)}, {str(median)}, {str(stdev)}, {maxi}, {mini})"



if __name__ == "__main__":
    inrto()                         # Print animation 
    candCount: int                  # Number of Total Candidates 
    candPassed: int                 # Number of selected Candidates
    distibutionType: Dist           # Random Numbers Distribution
    luckPercentage: float           # Luck Percentage to Scale The Random Probabilities
    a, b= 0, 0                      # Default values for Beta distribution


    # Input values from the user ... 
    try: 
        candCount = int(input("[-] Enter the number of candidates: "))
        candPassed = int(input("[-] Enter the number of successful candidates: "))
        luckPercentage = float(input("[-] Enter the luck percentage for each candidate (E.g. 0.05): "))
        distibutionType = Dist[input("[-] Enter the distribution of random numbers (Beta/Uniform): ").upper()]
        if distibutionType == Dist.BETA:
            a = float(input("[-] Alpha Parameter: "))
            b = float(input("[-] Beta Parameter: "))
    except:
        print("[!] The distribution is not exit!")
        exit()


    print("***")
    print("***")
    print("***")
    print(f"[*] Number of times to perform the simulation: {NUMBER_OF_SIMULATION}")
    finalDicBasedOnOverallScore, finalDicBasedOnHardWorking = toySim(candCount, candPassed, luckPercentage, distibutionType, a, b)
    print("\n***")
    print("***")
    print("***")


    # Calculate Statistics of Hard Working and Luck Based For Selected Astronauts 
    hardWorkValues = []
    luckValues = []
    for simNum in range(0, NUMBER_OF_SIMULATION):
        for candNum in range(0, candPassed):
            hardWorkValues.append(finalDicBasedOnOverallScore[simNum][candNum][1] / (1 - luckPercentage))
            luckValues.append(finalDicBasedOnOverallScore[simNum][candNum][2] / luckPercentage)
    print(f"[+] The (mean, median, STD, max, min) for the hard working values of the selected astronauts: {calcStatistics(hardWorkValues)}")
    print(f"[+] The (mean, median, STD, max, min) for the luck values of the selected astronauts: {calcStatistics(luckValues)}")
    
    
    # Calculate Number of Selected Astronauts Based on Skill Alone
    commonCand = []
    for simNum in range(0, NUMBER_OF_SIMULATION):
        sim1 = finalDicBasedOnOverallScore[simNum]
        sim2 = finalDicBasedOnHardWorking[simNum]

        common = 0
        for x in range(0, candPassed):
            for y in range(0, candPassed):
                if sim1[x] == sim2[y]:
                    common += 1

        commonCand.append(common)
    print(f"[+] The (mean, median, STD, max, min) for the number of selected astronauts based on skill alone: {calcStatistics(commonCand)}")
    
    
    # Calculate Statistics of Hard Working and Luck Values For Selected Astronauts Based on Skill Alone
    hardWorkValues = []
    luckValues = []
    for simNum in range(0, NUMBER_OF_SIMULATION):
        for candNum in range(0, candPassed):
            hardWorkValues.append(finalDicBasedOnHardWorking[simNum][candNum][1] / (1 - luckPercentage))
            luckValues.append(finalDicBasedOnHardWorking[simNum][candNum][2] / luckPercentage)
    print(f"[+] The (mean, median, STD, max, min) for hard working of selected astronauts based on skill alone: {calcStatistics(hardWorkValues)}")
    print(f"[+] The (mean, median, STD, max, min) for luck of selected astronauts based on skill alone: {calcStatistics(luckValues)}")
