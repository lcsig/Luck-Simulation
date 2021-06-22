# Luck-Simulation
"Is Success Luck or Hard Work?" that was a title of a video made by Derek Muller.

He argued that "The importance of luck increases the greater the number of applicants applying for just a few spaces. Consider the most recent class of NASA astronauts. From over 18,300 applicants in 2017, only 11 were selected and went on to graduate from the astronaut training program. Now we can make a toy model of the selection process. Let's assume that astronauts are selected mostly based on skill, experience, and hard work, but also say five percent as a result of luck — fortunate circumstances. For each applicant, I randomly generated a skill score out of a hundred,  and I also randomly generated a luck score out of a hundred. Then I added those numbers together, weighted in the 95-to-5 ratio to get an overall score. This score represents the selector's judgments, meaning the top 11 by this metric would become astronauts. And I repeated this simulation a thousand times representing a thousand different astronaut selections. And what I found was the astronauts who were picked were very lucky; they had an average luck score of 94.7. So how many of the selected astronauts would have been in the top 11 based on skill alone? The answer was, on average, only 1.6. That means, even with luck accounting for just 5% of the outcome, 9 or maybe 10 of the 11 applicants selected would have been different if luck played no role at all. When competition is fierce, being talented and hard-working is important, but it's not enough to guarantee success. You also need to catch a break. Largely, I think we're unaware of our good luck because, by definition, it's not something we did. Like the housework done by your significant other, it goes unappreciated. And here's the crazy thing: Downplaying the importance of chance events may actually improve your probability of success because if you perceive an outcome to be uncertain, you're less likely to invest effort in it, which further decreases your chances of success. So, it's a useful delusion to believe you are in full control of your destiny."

# Results 
## Uniform Distribution | 5% Luck Percentage
```
#############################################################
#                                                           #
#                       NASA Astronauts                     #
#                                                           #
#############################################################
[-] Enter the number of candidates: 18300
[-] Enter the number of successful candidates: 11
[-] Enter the luck percentage for each candidate (E.g. 0.05): 0.05
[-] Enter the distribution of random numbers (Beta/Uniform): uniform
***
***
***
[*] Number of times to perform the simulation: 10000
.......|
***
***
***
[+] The (mean, median, STD, max, min) for the hard working values of the selected astronauts: (0.9973, 0.9977, 0.002, 1.0, 0.9889)
[+] The (mean, median, STD, max, min) for the luck values of the selected astronauts: (0.9479, 0.955, 0.038, 1.0, 0.781)
[+] The (mean, median, STD, max, min) for the number of selected astronauts based on skill alone: (1.5813, 1.0, 1.1056, 6, 0)
[+] The (mean, median, STD, max, min) for hard working of selected astronauts based on skill alone: (0.9997, 0.9998, 0.0002, 1.0, 0.9986)
[+] The (mean, median, STD, max, min) for luck of selected astronauts based on skill alone: (0.4995, 0.4986, 0.2883, 1.0, 0.0)
```
## Uniform Distribution | 1% Luck Percentage
```
#############################################################
#                                                           #
#                       NASA Astronauts                     #
#                                                           #
#############################################################
[-] Enter the number of candidates: 18300
[-] Enter the number of successful candidates: 11
[-] Enter the luck percentage for each candidate (E.g. 0.05): 0.01
[-] Enter the distribution of random numbers (Beta/Uniform): uniform
***
***
***
[*] Number of times to perform the simulation: 10000
.......|
***
***
***
[+] The (mean, median, STD, max, min) for the hard working values of the selected astronauts: (0.9989, 0.999, 0.0009, 1.0, 0.995)
[+] The (mean, median, STD, max, min) for the luck values of the selected astronauts: (0.881, 0.8969, 0.0866, 1.0, 0.4832)
[+] The (mean, median, STD, max, min) for the number of selected astronauts based on skill alone: (3.4592, 3.0, 1.3688, 8, 0)
[+] The (mean, median, STD, max, min) for hard working of selected astronauts based on skill alone: (0.9997, 0.9998, 0.0002, 1.0, 0.9983)
[+] The (mean, median, STD, max, min) for luck of selected astronauts based on skill alone: (0.5008, 0.5005, 0.2887, 1.0, 0.0)
```
## Beta Distribution | 5% Luck Percentage
```
#############################################################
#                                                           #
#                       NASA Astronauts                     #
#                                                           #
#############################################################
[-] Enter the number of candidates: 18300
[-] Enter the number of successful candidates: 11
[-] Enter the luck percentage for each candidate (E.g. 0.05): 0.05
[-] Enter the distribution of random numbers (Beta/Uniform): beta
[-] Alpha Parameter: 4
[-] Beta Parameter: 4
***
***
***
[*] Number of times to perform the simulation: 10000
.......|
***
***
***
[+] The (mean, median, STD, max, min) for the hard working values of the selected astronauts: (0.9751, 0.9751, 0.0159, 1.0, 0.9153)
[+] The (mean, median, STD, max, min) for the luck values of the selected astronauts: (0.5857, 0.5948, 0.1693, 1.0, 0.0)
[+] The (mean, median, STD, max, min) for the number of selected astronauts based on skill alone: (8.6872, 9.0, 1.0253, 11, 4)
[+] The (mean, median, STD, max, min) for hard working of selected astronauts based on skill alone: (0.9773, 0.9768, 0.0139, 1.0, 0.927)
[+] The (mean, median, STD, max, min) for luck of selected astronauts based on skill alone: (0.5001, 0.5003, 0.1785, 1.0, 0.0)
```
## Beta Distribution | 1% Luck Percentage
```
#############################################################
#                                                           #
#                       NASA Astronauts                     #
#                                                           #
#############################################################
[-] Enter the number of candidates: 18300
[-] Enter the number of successful candidates: 11
[-] Enter the luck percentage for each candidate (E.g. 0.05): 0.01
[-] Enter the distribution of random numbers (Beta/Uniform): beta
[-] Alpha Parameter: 4
[-] Beta Parameter: 4
***
***
***
[*] Number of times to perform the simulation: 10000
.......|
***
***
***
[+] The (mean, median, STD, max, min) for the hard working values of the selected astronauts: (0.9771, 0.9767, 0.0141, 1.0, 0.9229)
[+] The (mean, median, STD, max, min) for the luck values of the selected astronauts: (0.5169, 0.5192, 0.1782, 1.0, 0.0)
[+] The (mean, median, STD, max, min) for the number of selected astronauts based on skill alone: (10.4955, 11.0, 0.5833, 11, 8)
[+] The (mean, median, STD, max, min) for hard working of selected astronauts based on skill alone: (0.9772, 0.9767, 0.014, 1.0, 0.9242)
[+] The (mean, median, STD, max, min) for luck of selected astronauts based on skill alone: (0.5005, 0.5013, 0.1787, 1.0, 0.0)
```

# Video 
https://www.youtube.com/watch?v=3LopI4YeC4I
