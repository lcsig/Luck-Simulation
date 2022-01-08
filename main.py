#!/bin/env python3
import random
import enum
import statistics
from numpy import random


NUMBER_OF_SIMULATION = 10000  # Number of times the simulation will be conducted
_STATISTICS_VALUES = "(mean, median, STD, max, min)"


class Dist(enum.Enum):  # Enum class to specify the distributions
    UNIFORM = 0
    BETA = 1


def intro():
    """
    A method that contains program
    """
    print("#############################################################")
    print("#                                                           #")
    print("#                       NASA Astronauts                     #")
    print("#                                                           #")
    print("#############################################################")


def gen_prob(n: int, distribution: Dist, a, b) -> list:
    """
    A function to generate n random number with certain distribution
    """
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


def toy_simulation(overall_candidates, candidates_who_passed, life_luck_percentage, random_distribution_type, a, b):
    """
    This method will perform the simulation and return two dictionaries
    The first dictionary is the selected astronauts based on the overall score
    The second dictionary is the selected astronauts based on the hardworking only
    Each astronaut is represented as a list of [Luck + HardWorking, HardWorking Value, Luck Value]
    """
    final_dic_based_on_overall_score = {}
    final_dic_based_on_hard_working = {}

    for numSim in range(0, NUMBER_OF_SIMULATION):

        # Generate Random Numbers
        hard_working_list = gen_prob(overall_candidates, random_distribution_type, a, b)
        luck_list = gen_prob(overall_candidates, random_distribution_type, a, b)

        temp_dict = []
        # Scale and Add up
        for i in range(0, overall_candidates):
            luck_list[i] = luck_list[i] * life_luck_percentage
            hard_working_list[i] = hard_working_list[i] * (1 - life_luck_percentage)
            temp_dict.append([luck_list[i] + hard_working_list[i], hard_working_list[i], luck_list[i]])

        # Sort and Get the top astronauts based on the over all score
        sorted_values = sorted(temp_dict, key=lambda x: x[0])
        sorted_values.reverse()
        final_dic_based_on_overall_score[numSim] = sorted_values[0:candidates_who_passed]

        # Sort and Get the top astronauts based on hard working only
        sorted_values = sorted(temp_dict, key=lambda x: x[1])
        sorted_values.reverse()
        final_dic_based_on_hard_working[numSim] = sorted_values[0:candidates_who_passed]

        # Progress ...
        if numSim % 4 == 0:
            print(f"---> [/] ---> {round((numSim / NUMBER_OF_SIMULATION) * 100, 2)}%", end='\r')
        elif numSim % 4 == 1:
            print(f"---> [-] ---> {round((numSim / NUMBER_OF_SIMULATION) * 100, 2)}%", end='\r')
        elif numSim % 4 == 2:
            print(f"---> [\\] ---> {round((numSim / NUMBER_OF_SIMULATION) * 100, 2)}%", end='\r')
        elif numSim % 4 == 3:
            print(f"---> [|] ---> {round((numSim / NUMBER_OF_SIMULATION) * 100, 2)}%", end='\r')

    return final_dic_based_on_overall_score, final_dic_based_on_hard_working


# A method to calculate max, min, mean, median, std and return them as a string
def calc_statistics(arr):
    mean = round(statistics.mean(arr), 4)
    median = round(statistics.median(arr), 4)
    stdev = round(statistics.stdev(arr), 4)
    maxi = round(max(arr), 4)
    mini = round(min(arr), 4)

    return f"({str(mean)}, {str(median)}, {str(stdev)}, {maxi}, {mini})"


def get_hard_working_and_luck_values(toy_simulation_dict: dict, candidates_passed: int, luck_percentage: float):
    hard_work_values = []
    luck_values = []

    for simulation_num in range(0, NUMBER_OF_SIMULATION):
        for candidate_num in range(0, candidates_passed):
            hard_work_values.append(toy_simulation_dict[simulation_num][candidate_num][1] / (1 - luck_percentage))
            luck_values.append(toy_simulation_dict[simulation_num][candidate_num][2] / luck_percentage)

    return hard_work_values, luck_values


if __name__ == "__main__":
    intro()  # Print animation
    candidates_count: int  # Number of Total Candidates
    candidates_passed: int  # Number of selected Candidates
    distribution_type: Dist  # Random Numbers Distribution
    luck_percentage: float  # Luck Percentage to Scale The Random Probabilities
    a, b = 0, 0  # Default values for Beta distribution

    # Input values from the user ...
    try:
        candidates_count = int(input("[-] Enter the number of candidates: "))
        candidates_passed = int(input("[-] Enter the number of successful candidates: "))
        luck_percentage = float(input("[-] Enter the luck percentage for each candidate (E.g. 0.05): "))
        distribution_type = Dist[input("[-] Enter the distribution of random numbers (Beta/Uniform): ").upper()]

        if distribution_type == Dist.BETA:
            a = float(input("[-] Alpha Parameter: "))
            b = float(input("[-] Beta Parameter: "))
    except:
        print("[!] The distribution is not exit!")
        exit()

    print("***")
    print("***")
    print("***")
    print(f"[*] Number of times to perform the simulation: {NUMBER_OF_SIMULATION}")
    dict_based_on_overall_score, dict_based_on_hard_working = toy_simulation(candidates_count,
                                                                             candidates_passed,
                                                                             luck_percentage,
                                                                             distribution_type, a, b
                                                                             )
    print("")
    print("***")
    print("***")
    print("***")

    # Calculate Statistics of Hard Working and Luck Based For Selected Astronauts
    hard_work_values, luck_values = get_hard_working_and_luck_values(dict_based_on_overall_score,
                                                                     candidates_passed,
                                                                     luck_percentage)

    # Calculate Statistics of Hard Working and Luck Values For Selected Astronauts Based on Skill Alone
    hard_work_values_skill_alone, luck_values_skill_alone = get_hard_working_and_luck_values(dict_based_on_hard_working,
                                                                                             candidates_passed,
                                                                                             luck_percentage)

    # Calculate Number of Selected Astronauts Based on Skill Alone
    common_candidates = []
    for simulation_num in range(0, NUMBER_OF_SIMULATION):
        sim1 = dict_based_on_overall_score[simulation_num]
        sim2 = dict_based_on_hard_working[simulation_num]
        common = 0
        for x in range(0, candidates_passed):
            for y in range(0, candidates_passed):
                if sim1[x] == sim2[y]:
                    common += 1
        common_candidates.append(common)

    print(f"[+] The {_STATISTICS_VALUES} for the hard working values of the selected astronauts: "
          f"{calc_statistics(hard_work_values)}")
    print(f"[+] The {_STATISTICS_VALUES} for the luck values of the selected astronauts: "
          f"{calc_statistics(luck_values)}")

    print(f"[+] The {_STATISTICS_VALUES} for the number of selected astronauts based on skill alone: "
          f"{calc_statistics(common_candidates)}")

    print(f"[+] The {_STATISTICS_VALUES} for the hard working values of the selected astronauts based on skill alone: "
          f"{calc_statistics(hard_work_values_skill_alone)}")
    print(f"[+] The {_STATISTICS_VALUES} for the luck values of the selected astronauts based on skill alone: "
          f"{calc_statistics(luck_values_skill_alone)}")
