# Rational Approximator
# Using the Farey algorithm
# Inspired by Stand-up Maths video titled 'Why do calculators get this wrong? (We don't know!)' uploaded on Jul 16, 2020

# Farey Algorithm: Given two fractions, will output some fraction in between them

import math

# IMPORTANT GLOBAL PROGRAM SETTINGS
print_in_loop = True                        # Whether or not to print comments as it calculates each iteration (MAJOR SLOW-DOWN)                False is faster.
num_of_iterations = 100000                  # How far down the rabbit-hole?                                                                     A million gets quite slow...
max_denom = float('inf')                    # Max allowed denominator.                                                                          Put  float('inf')  for no effect.
reasonable_error = 0                        # If the approximation is this far away from the real value, halt program (but don't catch fire).   Set to 0 (ZERO) for no effect.


def main():
    print('Rational Approximator')
    print('Created by Lens of Lensor Radii')
    print()
    get_input()


def get_input():
    print('Please enter a number to approximate')
    print()
    uIn1_str = input()
    try:
        uIn1_flt = float(uIn1_str)
    except:
        print('INCORRECT INPUT')
        print()
        print('Try again')
        print()
        get_input()
    else:
        run_farey(uIn1_flt)


def run_farey(origin):
    decimal = get_abs_decimal(origin)
    print(); print('Found decimal as: '); print(decimal); print()
    if decimal == 0:
        print()
        print('Decimal is ZERO (0). Exact number found.')
        print()
        print()
        print('****************************************************************************************************************')
        print('EXACT APPROXIMATION: ', origin)
        print()
        print('****************************************************************************************************************')
        print()
        print('RESTARTING')
        print()
        get_input()
    else:
        # num = Numerator
        # denom = Denominator

        farey1_num = 0
        farey1_denom = 1

        farey2_num = 1
        farey2_denom = 1

        next_farey_num = 0
        next_farey_denom = 0
        next_farey_dec = 0
        next_farey_diff = 0
        next_farey_diff_perc = 0

        for i in range(num_of_iterations):
            i_save = i
            next_farey_num = farey1_num + farey2_num
            next_farey_denom = farey1_denom + farey2_denom
            if next_farey_denom > max_denom:
                print()
                print('****************************************************************************************************************')
                print('MAX ALLOWED DENOMINATOR REACHED')
                print()
                next_farey_num = last_farey_num
                next_farey_denom = last_farey_denom
                next_farey_dec = last_farey_dec
                next_farey_diff = last_farey_diff
                next_farey_diff_perc = last_farey_diff_perc
                break

            next_farey_dec = next_farey_num/next_farey_denom
            if next_farey_dec == decimal:
                print()
                print('****************************************************************************************************************')
                print('FOUND EXACT FRACTION')
                print()
                break;

            next_farey_diff = next_farey_dec - decimal
            if abs(next_farey_diff) < reasonable_error:
                print()
                print('****************************************************************************************************************')
                print('WITHIN REASONABLE AMOUNT OF ERROR')
                print()
                break;

            next_farey_diff_perc = ((next_farey_diff) / next_farey_dec) * 100

            if (print_in_loop):
                print()
                print('Iteration: ', i)
                print('APPROXIMATION: ', next_farey_num, '/', next_farey_denom)
                print('APPROXIMATION (dec): ', next_farey_dec)
                print('DIFFERENCE (%): ', next_farey_diff_perc)
                print('DIFFERENCE (dec): ', next_farey_diff)
                print()

            last_farey_num = next_farey_num
            last_farey_denom = next_farey_denom
            last_farey_dec = next_farey_dec
            last_farey_diff = next_farey_diff
            last_farey_diff_perc = next_farey_diff_perc

            tmp1 = get_closer_value(decimal, (farey2_num/farey2_denom), (next_farey_num/next_farey_denom))

            if tmp1 == 'small':
                farey2_num = next_farey_num
                farey2_denom = next_farey_denom
            elif tmp1 == 'large':
                farey1_num = next_farey_num
                farey1_denom = next_farey_denom

        print('****************************************************************************************************************')
        print('FINISHED!')
        print()
        print('****************************************************************************************************************')
        print('Starting Decimal: ', decimal)
        print()
        print('Best Approximation Found: ', next_farey_num, '/', next_farey_denom)
        print('Decimal Approximation: ', next_farey_dec)
        print('Final Number: ', math.trunc(origin), ' and ', next_farey_num, '/', next_farey_denom)
        print()
        print('Decimal Error: ', f'{next_farey_diff:.18f}')
        print('Scientific Notation Error: ', next_farey_diff)
        print('Percentage Error: ', f'{next_farey_diff_perc:.18f}', '%')
        print()
        print('Iterations Used: ', i_save)
        print()
        for i in range(12):
            print()


def get_closer_value(dec, lrg, nxt_farey):
    diff_lrg = abs(lrg - dec)
    nxt_diff_lrg = abs(lrg - nxt_farey)

    if diff_lrg < nxt_diff_lrg:
        return 'large'
    else:
        return 'small'
        

def get_abs_decimal(number):
    truncated = math.trunc(number)
    return abs(number - truncated)


if __name__ == '__main__':
    main()