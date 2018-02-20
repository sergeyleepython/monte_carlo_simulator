import serial
from dashboard import DATAFLOW


def run_sensors():
    with serial.Serial('/dev/ttyACM0', 9600) as ser:

        while True:

            line = ser.readline()
            line = line.decode('utf-8')
            # print(line)
            try:
                wheel, value = line.split()
            except ValueError:
                wheel = 'FL'
                value = 0.5
            value = float(value)
            print(wheel, value)
            # try:
            DATAFLOW['Vibration ' + wheel].append(value)
            # except KeyError:
            #     pass
            # if len(DATAFLOW[wheel]) < 10:
            #     DATAFLOW[wheel].append(value)
            # else:
            #     print(DATAFLOW[wheel])
            #     DATAFLOW[wheel] = []


import random
import time


def dump_sensors():
    while True:
        time.sleep(0.1)
        value = random.uniform(0, 5)
        DATAFLOW['Vibration FL'].append(value)
        DATAFLOW['Vibration FR'].append(value)
        DATAFLOW['Vibration RL'].append(value)
        DATAFLOW['Vibration RR'].append(value)
