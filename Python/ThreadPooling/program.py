import concurrent.futures as con_fu
import random as rng
import time


should_use_threads = True
should_time = True

should_input_use_threads = False
should_input_iter = True

iterations = 10
wait_min = 1  # Minimum number of seconds to pass to the wait_for function
wait_max = 10  # Maximum number of seconds to pass to the wait_for function


def wait_for(seconds):  # Waits for a given amount of time
    print(f'START! Waiting for {seconds}s')
    time.sleep(seconds)  # zZZzzZZZZzzzZzzZZZzzz
    return f'DONE! Waited for {seconds}s'


def main():
    global iterations
    global should_use_threads

    if should_input_iter:
        while True:
            input_iter = input('Enter Number of Threads: ')
            try:
                iterations = int(input_iter)
                break
            except ValueError or TypeError:
                print('\nINVALID INPUT\n')
                continue

    if should_input_use_threads:
        while True:
            input_use_threads = input('Use Multiple Threads? ')
            if 'y' in input_use_threads or '1' in input_use_threads or 't' in input_use_threads:
                should_use_threads = True
            elif 'n' in input_use_threads or '0' in input_use_threads or 'f' in input_use_threads:
                should_use_threads = False
            else:
                print('\nINVALID INPUT\n')
                continue

    if should_time: start = time.perf_counter_ns() # Get Start Time for Computation Duration
    if should_use_threads:
        with con_fu.ThreadPoolExecutor() as executor:  # Create ThreadPool Executor object
            results = []
            for _ in range(iterations):
                rand_wait = rng.randint(wait_min, wait_max)  # Get random number of seconds to wait
                results.append(executor.submit(wait_for, rand_wait))

            for f in con_fu.as_completed(results):  # Print Results as they come in (On Function Complete aka return)
                print(f.result())
    else:
        for _ in range(iterations):
            rand_wait = rng.randint(wait_min, wait_max)  # Get random number of seconds to wait
            print(wait_for(rand_wait))

    if should_time:
        finish = time.perf_counter_ns()  # Get End Time of Total Computation Duration
        duration = finish - start
        print('\n\nDuration: \n'
              f'{duration}ns\n'
              f'{duration / 1000}µs\n'
              f'{duration / 1000000}ms\n'
              f'{duration / 1000000000}s\n'
              '\n\n')
    print('ALL DONE')


if __name__ == '__main__':
    main()
