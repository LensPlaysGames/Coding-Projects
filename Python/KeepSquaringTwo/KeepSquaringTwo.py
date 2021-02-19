'''
A program that keeps squaring two, then does that some more. See how high you can get, how fast!

A program made by Lens of Lensor Radii
'''

def main():
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print()
    print('KEEP SQUARING TWO')
    print()
    print('by')
    print('Lens')
    print()
    print('of')
    print('Lensor Radii')
    print()
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

    starting_number = get_start_num()
    input()
    run_loop(starting_number)


def get_start_num():
    got_input = False
    while got_input == False:
        print('Please enter a positive number')
        number = input()
        try:
            number = float(number)
            if number < 0:
                print()
                print('No negatives! Sneaky bugger...')
                print('Try again!')
                print()
                continue
            print('Starting Number Found as: ' + str(number))
        except Error as e:
            print()
            print('ERROR IN INPUT!')
            print(e)
            print()
            continue
        else:
            got_input = True
            break
    return number
    
            

def run_loop(start_num):
    print('STARTING NUMBER: ' + str(start_num))

    exponent = 0    

    while(True):
        try:
            last_num = start_num
            output = start_num ** exponent

            print()
            print(str(output) + ' = ' + str(last_num) + '^' + str(exponent))
            print()    

            exponent += 1
        except Error as e:
            print()
            print('ERROR IN CALCULATIONS!')
            print(e)
            print()
        


if __name__ == '__main__':
    main()