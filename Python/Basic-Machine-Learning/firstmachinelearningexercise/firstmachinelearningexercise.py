# Standard Python Libraries
import os.path
import pickle

# Data Formatting and Machine Learning
import pandas as pnds
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

# Data Visualization
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# THANK YOU TO UCI FOR THE AMAZING DATASETS :D
# https://archive.ics.uci.edu/ml/datasets/Student+Performance
# CODE BY LENS

train = False
amount_to_train = 10000

should_print = True
fine_print = True
plot = True

data = pnds.read_csv('student-mat.csv', sep=";")                                                            # Initialize data from Comma Seperated Values File
data = data[[                                                                                               # Remove Unused and Unnecessary Attributes in the Data to reduce size and increase speed
'G1',               # First Period Grade
'G2',               # Second Period Grade
'G3',               # Final Grade on a scale of 0-20
#'freetime',         # Rating of How Much Freetime after School on a scale of 1-5
#'studytime',        # Hours Student Studied per Week     
#'traveltime',       # 1 for Less Than Two hours, 2 for Two to Five hours, 3 for Five to Ten hours, or 4 for Greater Than Ten hours
#'goout',            # Rating of How Often Student Goes Out with Friends
'failures',         # Number of Classes Student has Failed Before
#'absences',         # Number of Days Student was Absent
#'famrel',           # Rating of how quality family relationships are on a scale of 1-5
#'Medu', 'Fedu'      # 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education)
'Dalc',             # Rating of Daily Alcohol Consumption on a scale of 1-5
'Walc',             # Rating of Weekly Alcohol Consumption on a scale of 1-5
#'health',           # Rating of Current Health Status on a scale of 1-5
]]

predict = 'G3'                                                                                              # Attribute in Data that the neural network will predict

x = np.array(data.drop([predict], 1))                                                                       # Removes Prediction from Training Data     (NO PEEKING!!! :D)
y = np.array(data[predict])                                                                                 # Correct Answers to Check against

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=.1)             # Splits Training And Test Data

if train:
    if should_print: print('STARTING TRAINING')

    best_score = 0
    for _ in range(amount_to_train):
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=.1)     # Splits Training And Test Data

        linear = linear_model.LinearRegression()                                                            # Creates Line of Best Fit Model (Accuracy)

        linear.fit(x_train, y_train)                                                                        # Input training data as Linear Model Input
        acc = linear.score(x_test, y_test)                                                                  # "Score" the Neural Network by comparing output to our correct data
        
        if fine_print:
            print('Accuracy: ')                                                                             # Just how good is this thing??
            print(acc, '\n')                                                                                # We'll See 🤷‍

        if acc > best_score:                                                                                # Overwrite File if Trained Model is Better than Previous Best Trained Model
            best_score = acc                                                                                # Update this Model to Previous Best Trained Model
            with open('student_MI_model.pickle', 'wb') as f:                                                # Open Pickle File
                pickle.dump(linear, f)                                                                      # Write Model to pickle file
                if print: print('\n///\n\nNew Best Model!!!\nAccuracy: ', acc, '\n\n///\n')                 # Print Accuracy of New Best Model
else:
    try:
        loaded_model = open('student_MI_model.pickle', 'rb')                                                # Load Model from File if not Training New Model(s)
        linear = pickle.load(loaded_model)
    except Exception as e:                                                                                  # Case Handling if File doesn't exist or there is some other issue
        print('\n///\n\nERROR FINDING MODEL PICKLE FILE!\nDoes it Even Exist⁉\nERROR MESSAGE: ', str(e), '\n\n///\n')

predictions = linear.predict(x_test)                                                                        # Store all Predictions to see what is influencing what :D

if should_print:
    print('\nP == Prediction')
    print('I == Input Data')
    print('C == Correct/Expected Output\n')                                                                 # also partners in crime   --   P.I.C. MOTHERFUCKER :D

    for x in range(len(predictions)):                                                                       # For Every Prediction Made by the Model
        print('\nPrediction: ', predictions[x], '\nInput: ', x_test[x], '\nCorrect: ', y_test[x], '\n')     # Print Prediction, Input Values, and The Expected Correct Value

    if train: print('\n\nFinal Accuracy: ', best_score)                                                     # How Good Were We Able to Get?

    print('\n\nCoeffecients: ')                                                                             # Importance of Each Attribute in the Prediction (Higher means more Influence)
    print(linear.coef_, '\n')                                                                               # The m in y=mx+b   --   Slope!
    print('Intercept: ')                                                                                    # 
    print(linear.intercept_, '\n\n')                                                                        # The b in y=mx+b  --   Intercept!

if plot:
    plt.style.use('ggplot')
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Math Students in Secondary Education in Portugal', fontsize=27)

    p1 = 'G2'                                                                                               # What to Compare Final Grade to in First Plot
    axs[0, 0].set_title('How Grades in Second Period Affect Final Grade')
    axs[0, 0].yaxis.set_major_locator(MultipleLocator(1))                                                   # NO DECIMALS
    axs[0, 0].set_xlabel(p1)
    axs[0, 0].set_ylabel(predict)

    axs[0, 0].scatter(data[p1], data[predict], zorder=10)                                                   # Plot Scatter Plot of p1 vs prediction

    m, b = np.polyfit(data[p1], data[predict], 1)                                                           # Calculate m and b of y=mx+b for Line of Best Fit
    axs[0, 0].plot(data[p1], m*data[p1]+b, 'b', label='Line of Best Fit')                                   # Plot Line of Best Fit

    axs[0, 0].legend()                                                                                      # Make a Legend


    p2 = 'failures'                                                                                         # What to Compare Final Grade to in Second Plot
    axs[0, 1].set_title('How Failures Affect Final Grade')
    axs[0, 1].yaxis.set_major_locator(MultipleLocator(1))                                                   # NO DECIMALS
    axs[0, 1].set_xlabel(p2)
    axs[0, 1].set_ylabel(predict)
    
    axs[0, 1].scatter(data[p2], data[predict], zorder=10)                                                   # Plot Scatter Plot of p2 vs prediction

    m, b = np.polyfit(data[p2], data[predict], 1)                                                           # Calculate m and b of y=mx+b for Line of Best Fit
    axs[0, 1].plot(data[p2], m*data[p2]+b, 'b', label='Line of Best Fit')                                   # Plot Line of Best Fit
    
    axs[0, 1].legend()                                                                                      # Make a Legend


    p3 = 'Dalc'                                                                                             # What to Compare Final Grade to in First Plot
    axs[1, 0].set_title('How Daily Alcohol Intake Affects Final Grade')
    axs[1, 0].yaxis.set_major_locator(MultipleLocator(1))                                                   # NO DECIMALS
    axs[1, 0].set_xlabel(p3)
    axs[1, 0].set_ylabel(predict)

    axs[1, 0].scatter(data[p3], data[predict], zorder=10)                                                   # Plot Scatter Plot of p3 vs prediction

    m, b = np.polyfit(data[p3], data[predict], 1)                                                           # Calculate m and b of y=mx+b for Line of Best Fit
    axs[1, 0].plot(data[p3], m*data[p3]+b, 'b', label='Line of Best Fit')                                   # Plot Line of Best Fit

    axs[1, 0].legend()                                                                                      # Make a Legend


    p4 = 'Walc'                                                                                             # What to Compare Final Grade to in Second Plot
    axs[1, 1].set_title('How Weekly Alcohol Intake Affects Final Grade')
    axs[1, 1].yaxis.set_major_locator(MultipleLocator(1))                                                   # NO DECIMALS
    axs[1, 1].set_xlabel(p4)
    axs[1, 1].set_ylabel(predict)
    
    axs[1, 1].scatter(data[p4], data[predict], zorder=10)                                                   # Plot Scatter Plot of p4 vs prediction

    m, b = np.polyfit(data[p4], data[predict], 1)                                                           # Calculate m and b of y=mx+b for Line of Best Fit
    axs[1, 1].plot(data[p4], m*data[p4]+b, 'b', label='Line of Best Fit')                                   # Plot Line of Best Fit
    
    axs[1, 1].legend()                                                                                      # Make a Legend
    

    plt.gcf().set_size_inches(12, 9)                                                                        # Set Default Plot Size
    plt.tight_layout(pad=2.4)                                                                               # NO OVERLAP
    plt.show()                                                                                              # Display Figure