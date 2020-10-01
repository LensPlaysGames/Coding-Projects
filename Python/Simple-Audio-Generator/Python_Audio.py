"""
Title: Simple-Audio-Generator
Desc: Generate 2-Second-Long Clips of Audio in Root Directory at a Given Frequency

CODE BY LENS
"""

import numpy as np; from numpy import random as rand
import scipy as sp; from scipy import signal as sig
import wave
import struct
import math
import sys

sample_width = 2 # bits per sample
sample_rate = 44100
length = sample_rate * 2

dflt_freq = 440

def main():
    print()
    print("Welcome to Lens' Audio Generator!!")
    print()
    print("Version: v0.1.0")
    print("Python: " + "v" + sys.version)
    print("Numpy: " + "v" + np.__version__)
    print()

    print()
    print("Please Input Frequency Between 20 and 20000")
    print()

    input_Freq = input()

    if (input_Freq == ""):
        print("USING DEFAULT FREQ: " + str(dflt_freq))
        freq = dflt_freq
    elif not (is_int(input_Freq)) or (int(input_Freq) < 20) or (int(input_Freq) > 20000):
        print()
        print("INCORRECT INPUT FORMAT")
        print("RESTARTING")
        print()
        main()
    else:
        freq = int(input_Freq);
        print("Setting Frequency to: " + str(freq))

    print()
    write_audio("white_noise", define_samples(random_samples))
    write_audio("sine", define_samples(sine_samples, freq))
    write_audio("square", define_samples(square_samples, freq))
    write_audio("sawtooth", define_samples(saw_samples, freq))
    write_audio("cool", define_samples(cool_samples, freq))

    print()
    print("Getting ALL da values")
    values = define_samples(random_samples)
    values += define_samples(saw_samples)
    values += define_samples(sine_samples)

    write_audio("crazy", values)

def write_audio(file_name, values):
    try:
        print("Writing to " + file_name)
        wavfile = wave.open(file_name + ".wav", 'wb')
        wavfile.setparams((2, sample_width, sample_rate, 0, 'NONE', 'not compressed'))
        values_str = b''.join(values)
        wavfile.writeframes(values_str)
        print("Success! Wrote Audio to " + file_name)
    finally:
        wavfile.close


def define_samples(func, freq = 440):
    print()
    print("Creating " + func.__name__ + " at " + str(freq) + "hz")
    values = []
    for i in range(0, length):
        value = func(i, freq)
        if value < -128: value = -128
        elif value > 127: value = 127
        packed_value = struct.pack('b', value)
        for i in range(0, sample_width):
            values.append(packed_value)
    print("Created " + func.__name__ + " at " + str(freq) + "hz")
    return values

def random_samples(unused, _):
    return rand.randint(-128, 127)

def sine_samples(i, freq):
    return int(100 * np.sin(2 * np.pi * freq * i / sample_rate))

def square_samples(i, freq):
    return int(100 * sig.square(2 * np.pi * freq * i / sample_rate))

def saw_samples(i, freq):
    return int(100 * sig.sawtooth(2 * np.pi * freq * i / sample_rate))

def cool_samples(i, freq):
    return int(((100 * np.square(2 * np.pi * freq * i / sample_rate)) + (100 * sig.sawtooth(2 * np.pi * freq * i / sample_rate))) / 2)

def is_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

main()