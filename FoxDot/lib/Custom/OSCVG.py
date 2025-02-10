

from pythonosc.udp_client import SimpleUDPClient
import threading
import time


class OSCVG():
    def __init__(self, ip='127.0.0.1', port=65535):
        global code_text
        code_text = ''
        self.trig = False
        self.ip = ip
        self.port = port
        self.code = ""
        self.path = "videos/"
        self.file = ""
        self.thread_code = True
        self.lock = threading.Lock()
        self.thread_send_code = threading.Thread(target=self.send_code, daemon=True)
        self.thread_send_file = threading.Thread(target=self.send_file)
        self.client = SimpleUDPClient(self.ip, self.port)
        print("OSC Connection to " + self.ip + ": " + str(self.port) + " established.")
        self.thread_send_code.start()
        self.thread_send_file.start()

    @staticmethod
    def set_code_text(code):
        global code_text
        code_text = code

    def set_path(self, path):
        self.path = path
        print("New path to video files is >> " + self.path)

    def play(self, file):
        self.file = self.path + file
        self.send_file()

    def send_code(self):
        global code_text
        while self.thread_code:
            if code_text != self.code:
                self.client.send_message("/code", code_text)
                self.code = code_text
            time.sleep(0.1)

    def send_file(self):
        self.client.send_message("/video", self.file)

    def close(self):
        self.thread_code = False
        self.thread_send_code.join()
        self.thread_send_file.join()
        print("OSC connection to VizGlitch closed.")


# if __name__ == '__main__':
#     oscmsg = OSCVG()
#     oscmsg.send_file
