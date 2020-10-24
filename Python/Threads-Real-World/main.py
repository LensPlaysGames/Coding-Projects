"""
THIS SCRIPT DOWNLOADS IMAGES TO THE DIRECTORY IT IS IN (using Thread Pooling to Speed Up the Process)
ALSO TIMES THE TOTAL DURATION OF TIME SPENT DOWNLOADING AND LOGS IT TO duration.csv IF should_time IS TRUE
DOWNLOADS IMAGES AND WRITES DURATION iterations AMOUNT OF TIMES FOR EASY AUTOMATIC DATA COLLECTION

Thanks to Corey Schafer for the Great YouTube Tutorial and the Image Urls!
YouTube Tutorial:   https://www.youtube.com/watch?v=IEEhzQoKtQU
Image Urls:         https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Threading/download-images.py
"""

import requests
import time
import csv
import os.path
import concurrent.futures as conc_fut

should_time = True  # Should the Program Time the Total Time Spent Downloading
should_print = True  # Should the Program Print to the Console as it Downloads
should_save = True  # Should the Program Save the Duration Time to a CSV file called 'durations.csv'
iterations = 50  # How many times should the images be downloaded (and therefore timed)

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c',
    'https://images.unsplash.com/photo-1602525968752-43f2d69250b4',
    'https://picsum.photos/200/300',
    'https://picsum.photos/300/200',
    'https://picsum.photos/100/200',
    'https://picsum.photos/200/100',
    'https://picsum.photos/300/300',
    'https://picsum.photos/200/200',
    'https://picsum.photos/100/100',
]


def download_img(img_url):
    if should_print:
        print(f'Downloading {img_url}...')
    img_bytes = requests.get(img_url).content
    img_name = hex(hash(img_url))
    img_name = f'photo-{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        if should_print:
            print(f'{img_name} downloaded...')


def main():
    while True:
        should_use_threads = input('Use Multiple Threads to Download the Images? ')
        if 'y' in should_use_threads.lower() or '1' in should_use_threads or 't' in should_use_threads.lower():
            should_use_threads = True
            break
        elif 'n' in should_use_threads.lower() or '0' in should_use_threads or 'f' in should_use_threads.lower():
            should_use_threads = False
            break
        else:
            print('\n\nINVALID INPUT\n\n')
            continue

    for _ in range(iterations):
        if should_time:
            if should_print:
                print('Starting Timer')
            start = time.perf_counter_ns()

        if should_use_threads:
            with conc_fut.ThreadPoolExecutor() as executor:
                executor.map(download_img, img_urls)
        else:
            for img_url in img_urls:
                download_img(img_url)

        if should_time:
            finish = time.perf_counter_ns()
            if should_print:
                print('Timer Finished')
            duration = finish - start
            print('\n\nDuration:\n'
                  f'{duration}ns\n'
                  f'{duration / 1000}µs\n'
                  f'{duration / 1000000}ms\n'
                  f'{duration / 1000000000}s\n')
            if should_save:
                fields = {'Using Threads?': should_use_threads, 'Total Duration (s)': str(duration / 1000000000)}
                fieldnames = ['Using Threads?', 'Total Duration (s)']
                should_write_header = True
                filename = 'durations.csv'
                if os.path.exists(filename):
                    should_write_header = False
                else:
                    with open(filename, 'w') as f:
                        csv_dict_writer = csv.DictWriter(f, fieldnames=fieldnames)  # Open Dictionary Writer to File
                        csv_dict_writer.writeheader()  # Write Header to New File
                    print(f'Created {filename}')
                with open(filename, 'a+', newline='') as f:
                    # WRITE CSV
                    csv_dict_writer = csv.DictWriter(f, fieldnames=fieldnames)  # Open Dictionary Writer to File
                    csv_dict_writer.writerow(fields)  # Write Duration to End of File
                    if should_print:
                        print('\nWrote Duration to File!\n')
        print("ALL DONE")


if __name__ == "__main__":
    main()

