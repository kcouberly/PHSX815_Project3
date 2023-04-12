# PHSX815_Project3

Finding the most likely weight and uncertainty of a coin being tossed using simulated data

## Bernoulli.py

performs the simulated experiment and outputs as 'output.txt'

can alter weight of coin and number of tosses: run with -h to see inputs

## Analysis.py

plots a function proportional to the likelyhood and finds the maximum value of said function

the weight of the coin is the function parameter

plots the function based on the data outputted by Bernoulli.py 'output.txt'

prints the maximum value using scipy.optimize minimizer on the negation of the function

## Neyman_constructor.py

creates a neyman construction and prints the average value and standard deviation of a true value

run with -h to see inputs

can alter the number of flips per experiment as well as the number of experiments

uses analytic maximum of the function in Analysis.py to create measured values from data




