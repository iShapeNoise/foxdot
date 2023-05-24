#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import threading
import time


class RandomMachine():
    """
    Connect to Arduino and read duration
    """
    def __init__(self, port='/dev/ttyACM0', rate=9600):
        """
        Initializes the serial connection to the Arduino board
        """
        self.port = port
        self.rate = rate
        self.conn = serial.Serial(self.port, self.rate)
        self.reading = False
        self.duration = 0
        print("RandomMachine >> Initializing...")
        time.sleep(3)
        self.reading = True
        self.print_dur = False
        self.thread = threading.Thread(target=self.get_dur)
        self.thread.start()

    def read(self):
        """
        Start thread that reads
        """
        return self.duration

    def get_dur(self):
        """
        Function runs within thread. It reads lines of serial connection
        """
        while self.reading:
            self.duration = self.conn.readline().decode("utf-8").rstrip()
            if self.print_dur is True:
                print(self.duration)

    def tgl_print(self):
        if self.print_dur is False:
            self.print_dur = True
        if self.print_dur is True:
            self.print_dur = False

    def close(self):
        """
        To ensure we are properly closing our connection to the
        Arduino device.
        """
        self.reading = False
        self.thread.join()
        self.conn.close()
        print("RandomMachine closed.")


# if __name__ == '__main__':
#     rm = RandomMachine()
#     rm.read()
#     time.sleep(10)
#     rm.close()
