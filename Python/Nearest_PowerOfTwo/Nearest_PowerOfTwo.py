"""
NEAREST POWER OF 2
Put in any number and get the nearest power of 2. For computey-debuggy things, ya know?

Made by Lens, inspired by Matt Parker, who always gets so close, but, not quite ;). Here is my Parker Program.
"""

number = 0

def main():
    print("NEAREST POWER OF 2 COMPUTER THING PARKER PROGRAM WHOSAMAWHATSITS FUNCTION")
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print()

    got_input = False
    while got_input == False:
        number = input('Please enter your number: ')
        try:
            number = float(number)
            if number < 0:
                print()
                print('NO NEGATIVES! sneaky scoundrel... probably just trying to crash the program for fun!')
                print()
                continue
            print()
            print('Your number was found to be ' + str(number))
        except Error as e:
            print('ERROR')
            print(e)
            continue
        else:
            got_input = True
            break
    nearest_power_of_two, power_int, up_or_down, low, low_count, high, high_count = get_nearest_power_of_two(number)
    difference = abs(number - nearest_power_of_two)
    if difference != 0:
        end_of_output = ' and is ' + str(difference) + ' ' + up_or_down + ' your number'
    else:
        end_of_output = ' and is your number exactly!'
    print()
    print('THE NEAREST POWER OF TWO TO ' + str(number) + ' IS ' + str(nearest_power_of_two) + ' or 2^' + str(power_int) + end_of_output)
    print('')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('')
    print('Closest Power of Two Lower than ' + str(number) +' is ' + str(low) + ' or 2^' + str(low_count))
    print('Closest Power of Two Higher than ' + str(number) +' is ' + str(high) + ' or 2^' + str(high_count))
    print()

def get_nearest_power_of_two(num):
    low_bound = 0
    low_count = 0
    high_bound = 0
    high_count = 0
    
    while high_bound < num:
        high_count += 1
        high_bound = 2 ** high_count

    while low_bound < num:
        low_count += 1
        low_bound = 2 ** low_count

    low_count = low_count - 1
    low_bound = low_bound - (low_bound - (2 ** low_count))

    diff_low = abs(low_bound - num)
    diff_high = abs(high_bound - num)
    
    if diff_low < diff_high:
        return low_bound, low_count, 'BELOW', low_bound, low_count, high_bound, high_count
    else:
        return high_bound, high_count, 'ABOVE', low_bound, low_count, high_bound, high_count


if __name__ == '__main__':
    main()
