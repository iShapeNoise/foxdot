#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import interp
import argparse
import math
import serial
import threading
import time


class MindStalker():
    """
    Connect to MindStalker RPi and read brainwave data every second
    """
    def __init__(self, port='/dev/ttyUSB0', rate=57600):
        """
        Initializes the serial connection to the Arduino board
        """
        self.port = port
        self.rate = rate
        self.conn = serial.Serial(self.port, self.rate)
        print("MindStalker >> Initializing...")
        time.sleep(3)
        self.freqs = []
        self.reading = True
        self.print_freqs = False
        self.thread = threading.Thread(target=self.get_freqs)
        self.thread.start()

    def read(self):
        """
        Get frequency values
        """
        return self.freqs

    def get_freqs(self):
        """
        Function runs within thread. It reads lines of serial connection
        """
        while self.reading:
            self.input = self.conn.readline()
            print(self.input)
            # if len(self.input) > 2:
            #     self.freqs = []
            #     self.output = [int(i) for i in self.input.decode().split(',')]
            #     self.freqs.append(self.output)
            #     #     var(interp(self.output[3], [3000, 3000000], [-12, 12])))
            #     # var.wTwo = var(interp(msg[4],[3000, 3000000], [-12, 12]))
            #     # var.wThree = var(interp(msg[5],[3000, 3000000], [-12, 12]))
            #     # var.wFour = var(interp(msg[6],[3000, 3000000], [-12, 12]))
            #     # var.wFive = var(interp(msg[7],[3000, 3000000], [-12, 12]))
            #     # var.wSix = var(interp(msg[8],[3000, 3000000], [-12, 12]))
            #     # var.wSeven = var(interp(msg[9],[3000, 3000000], [-12, 12]))
            #     # var.wEight = var(interp(msg[10],[3000, 3000000], [-12, 12]))
            #     # print(msg[3:11])
            # if self.print_freqs:
            #     print(self.freqs)

    def tgl_print(self):
        if self.print_freqs is False:
            self.print_freqs = True
        if self.print_freqs is True:
            self.print_freqs = False

    def close(self):
        """
        To ensure we are properly closing our connection to the
        Arduino device.
        """
        self.reading = False
        self.thread.join()
        self.conn.close()
        print("MindStalker closed.")


# if __name__ == '__main__':
#     ms = MindStalker()
#     ms.read()
#     time.sleep(10)
#     ms.close()
