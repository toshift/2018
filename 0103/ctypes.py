from ctypes import *
from ctypes.wintypes import MSG
from ctypes.wintypes import DWORD

import threading
import time
import datetime

class Hoge:
  def __init__(self):
    self.lUser32 = user32
  def installHookProc(self, pointer):
    self.hooked = self.lUser32.SetWindowsHookExA(
        WH_KEYBOARD_LL,
        pointer,
        kernel32.GetModuleHandleW(None),
        0
    )
 
  def uninstallHookProc(self):
    self.lUser32.UnhookWindowsHookEx(self.hooked)
    self.hooked = None


class TestThread(threading.Thread):

    """docstring for TestThread"""

    def __init__(self, n, t):
        super(TestThread, self).__init__()
        self.n = n
        self.t = t

    def run(self):
        print (" === start sub thread (sub class) === ")
        for i in range(self.n):
            time.sleep(self.t)
            print ("sub thread (sub class) : " + str(datetime.datetime.today()))
        print (" === end sub thread (sub class) === ")

if __name__ == "__main__":
    TestThread()
