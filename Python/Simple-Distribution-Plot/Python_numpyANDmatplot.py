import numpy as np; from numpy import random as r
import matplotlib.pyplot as mpl
import timeit; from timeit import default_timer as timer

def isInt(q):
    try:
        int(q)
        return True
    except ValueError:
        return False

def main():
    start = timer()

    startupMessage = "Welcome! to Ry Guy's (Lens) ULTIMATE USELESS PYTHON PROGRAM"

    print()
    print(startupMessage)
    print()

    print()
    print("Type 0 to pick NORMAL DISTRIBUTION")
    print("Type 1 to pick UNIFORM DISTRIBUTION")
    print("Type 2 to pick GUMBEL DISTRIBUTION")
    print("Type 3 to pick LOGISTIC DISTRIBUTION")
    print("Type 4 to pick LAPLACE DISTRIBUTION")
    print("Type 5 to pick RAYLEIGH DISTRIBUTION")
    print()

    input_DistributionType = input()
    disttype = "Distribution Type Picked: "
    if not (isInt(input_DistributionType)):
        print()
        print("INCORRECT INPUT FORMAT: RESTARTING")
        print()
        main()

    elif (input_DistributionType == '0'):
        print()
        print(disttype + "NORMAL")
    elif (input_DistributionType == '1'):
        print()
        print(disttype + "UNIFORM")
    elif (input_DistributionType == '2'):
        print()
        print(disttype + "GUMBEL")
    elif (input_DistributionType == '3'):
        print()
        print(disttype + "LOGISTIC")
    elif (input_DistributionType == '4'):
        print()
        print(disttype + "LAPLACE")
    elif (input_DistributionType == '5'):
        print()
        print(disttype + "RAYLEIGH")
    else:
        print("Unrecognized Distribution Type, using Default: NORMAL")
        

    print()
    print("Type a Number to Set Data Set Size or No (n, no, NO, null) to Generate a random Data Set Size")
    print()

    input_DataSetSize = input()

    if 'n' in input_DataSetSize or 'N' in input_DataSetSize:
        dataSetSize = r.randint(10, 10000000)
    else:
        if (isInt(input_DataSetSize)):
            dataSetSize = int(input_DataSetSize)
        else:
            print()
            print("INCORRECT INPUT FORMAT: RESTARTING")
            print()
            main()

    print()
    print("Data Set Size: " + str(dataSetSize))
    print()
    print("Generating Numbers for Data Set Creation")
    print()

    mean = 100
    standardDeviation = r.randint(100)

    print()
    print("Mean: " + str(mean))
    print("Standard Deviation: " + str(standardDeviation))
    print()

    print()
    print("Generated Numbers for Data Set Creation")
    print("Generating Data Set")
    print()
    start1 = timer()
    if (input_DistributionType == '0'):
        rand = r.normal(mean, standardDeviation, dataSetSize)
    elif (input_DistributionType == '1'):
        rand = r.uniform(mean, standardDeviation, dataSetSize)
    elif (input_DistributionType == '2'):
        rand = r.gumbel(mean, standardDeviation, dataSetSize)
    elif (input_DistributionType == '3'):
        rand = r.logistic(mean, standardDeviation, dataSetSize)
    elif (input_DistributionType == '4'):
        rand = r.laplace(mean, standardDeviation, dataSetSize)
    elif (input_DistributionType == '5'):
        rand = r.rayleigh(mean, dataSetSize)
    else:
        print("Unrecognized Distribution Type, using Default: Normal")
        rand = r.normal(mean, standardDeviation, dataSetSize)

    elapsed1 = timer() - start1

    print()
    print("Time Elapsed: " + str(round(elapsed1, 2)) + "s")
    print("Generated Data Set")
    print("Plotting Data to Histogram")
    print()

    start2 = timer()
    mpl.hist(rand, mean)
    elapsed2 = timer() - start2

    print()
    print("Time Elapsed: " + str(round(elapsed2, 2)) + "s")
    print("Generated Histogram!")
    print("Visual to Data Time Elapsed Ratio: " + str(round((elapsed2 / elapsed1), 2)) + "x")
    print()

    mpl.show()

    print()
    print("RESTARTING")
    print()

    elapsed = timer() - start
    print()
    print("Total Time Elapsed: " + str(round(elapsed, 2)) + "s")
    print()

    main()

main()