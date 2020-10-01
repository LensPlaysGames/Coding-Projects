"""
Title: Simple-Distribution-Visualization
Desc: Visualize A Number of Different Distributions at a Given Input Size

CODE BY LENS
"""

import numpy as np; from numpy import random as r
import matplotlib.pyplot as mpl
import timeit; from timeit import default_timer as timer

def startup_info():
    print(); print("Welcome! to Ry Guy's (Lens) ULTIMATE USELESS PYTHON PROGRAM");
    print("V0.1.0"); print()

def isInt(q):
    try:
        int(q)
        return True
    except ValueError:
        return False

def restart(start, func):
    print(); print("RESTARTING"); print()

     # End Timer for Total Time in Program
    elapsed = timer() - start
     # And Display That Time
    print(); print("Total Time Elapsed: " + str(round(elapsed, 2)) + "s"); print()
    
     # Run passed Function (meant to restart main())
    func()

def get_dist_input():
    disttype = "Distribution Type Picked: "
    input_str = ""

     # Show All Options
    print(); print("Type 0 to pick NORMAL DISTRIBUTION")
    print("Type 1 to pick UNIFORM DISTRIBUTION")
    print("Type 2 to pick GUMBEL DISTRIBUTION")
    print("Type 3 to pick LOGISTIC DISTRIBUTION")
    print("Type 4 to pick LAPLACE DISTRIBUTION")
    print("Type 5 to pick RAYLEIGH DISTRIBUTION"); print()

     # Get Input
    input_str = input()
    
     # Check Input
    if not (isInt(input_str)):
        print(); print("INCORRECT INPUT FORMAT: RESTARTING"); print()
        restart(start, main())
    elif (input_str == '0'):
        print(); print(disttype + "NORMAL")
    elif (input_str == '1'):
        print(); print(disttype + "UNIFORM")
    elif (input_str == '2'):
        print(); print(disttype + "GUMBEL")
    elif (input_str == '3'):
        print(); print(disttype + "LOGISTIC")
    elif (input_str == '4'):
        print(); print(disttype + "LAPLACE")
    elif (input_str == '5'):
        print(); print(disttype + "RAYLEIGH")
    else:
        print("Unrecognized Distribution Type, using Default: NORMAL")

    return input_str

def get_size_input():
    data_size = 100
    input_str = ""
    print(); print("Type a Number to Set Data Set Size or No (n, no, NO, null) to Generate a random Data Set Size"); print()
    input_str = input()
    
    if 'n' in input_str or 'N' in input_str:
        data_size = r.randint(10, 10000000)
    else:
        if (isInt(input_str)):
            data_size = int(input_str)
        else:
            print()
            print("INCORRECT INPUT FORMAT: RESTARTING")
            print()
            main()

    print(); print("Data Set Size: " + str(data_size)); print()

    return data_size

def random_generation(dist_type, data_size):
    # Start Timer for Random Generation
    start1 = timer()

    print("Generating Data Set"); print()

    mean = r.randint(100, 999)
    print("Mean: " + str(mean)); print()

    standardDeviation = r.randint(100)
    print("Standard Deviation: " + str(standardDeviation)); print()

    # Random Gen based on Distribution Input
    if (dist_type == '0'):
        rand = r.normal(mean, standardDeviation, data_size)
    elif (dist_type == '1'):
        rand = r.uniform(mean, standardDeviation, data_size)
    elif (dist_type == '2'):
        rand = r.gumbel(mean, standardDeviation, data_size)
    elif (dist_type == '3'):
        rand = r.logistic(mean, standardDeviation, data_size)
    elif (dist_type == '4'):
        rand = r.laplace(mean, standardDeviation, data_size)
    elif (dist_type == '5'):
        rand = r.rayleigh(mean, data_size)
    else:
        print("Unrecognized Distribution Type, using Default: Normal")
        rand = r.normal(mean, standardDeviation, data_size)

    # End Timer for Random Generation
    elapsed1 = timer() - start1

    print(); print("Generated Data Set")
    print("Time Elapsed: " + str(round(elapsed1, 2)) + "s"); print()

    return rand

def main():
     # Display Startup Info
    startup_info()
     # Start Timer for Total Time in Program
    start = timer()

     # Get Input For Distribution to Use and How Many Numbers to Generate in that Distribution
    input_dist_type = get_dist_input()
    input_data_size = get_size_input()
    
    rand = random_generation(input_dist_type, input_data_size)

    print(); print("Plotting Data to Histogram"); print()

     # Start Timer for Plotting Data
    start2 = timer()
     # Plot Data to Histogram
    mpl.hist(rand, 100)
     # End Timer for Plotting Data
    elapsed2 = timer() - start2

     # Print Graph Generation Data
    print(); print("Generated Histogram!")
    print("Time Elapsed: " + str(round(elapsed2, 2)) + "s")

     # Display Plotted Graph!
    mpl.show()

     # Loop Program
    restart(start, main())

main()
