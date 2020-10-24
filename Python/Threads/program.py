import threading as th
import random as rng
import time

# SETUP
should_thread = False
iterations = 100

wait_min = 1
wait_max = 10


def foo(seconds):
    print(f'Waiting {seconds}s...')
    time.sleep(seconds)
    print(f'Waited {seconds}s')


# Boolean Input telling the program to Use (or Not Use) Threading
input_threads = input('Use Multi-Threading? ')  # Get Input
if 'y' in input_threads.lower() or '1' in input_threads or 't' in input_threads:  # Input Validation
    should_thread = True
else:
    should_thread = False

# Integer Input telling the program how many times
input_iter = input('Iterations to Test? ')  # Get Input
while True:  # Input Validation
    try:
        iterations = int(input_iter)
        break
    except ValueError or TypeError:
        print('\nINCORRECT INPUT, TRY AGAIN\n')
        continue

start = time.perf_counter_ns()  # Get Current Time in Nano-Seconds

if should_thread:
    threads = []  # Initialize List of Threads
    for _ in range(iterations):  # Do the thing, a lot
        rand = rng.randint(wait_min, wait_max)  # Get a random number of seconds to wait for
        t = th.Thread(target=foo, args=[rand])  # Create thread that will wait for rand amount of seconds
        threads.append(t)  # Add to List of Threads
        t.start()  # Start Thread

    for thread in threads:  # Bundles a Bunch of Asynchronous Threads so we can wait until all are done to move on
        thread.join()
else:
    for _ in range(iterations):
        foo(rng.randint(wait_min, wait_max))

finish = time.perf_counter_ns()  # Get Current Time in Nano-Seconds


duration = finish - start   # Get Total Duration of Computation in Nano Seconds
print(f'\n\nDuration: \n'
      f'{duration}ns\n'
      f'{duration/1000}µs\n'
      f'{duration/1000000}ms\n'
      f'{round((duration/1000000000), 2)}s'
      f'\n\n')  # Print Computation Duration
