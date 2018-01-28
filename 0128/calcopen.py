# coding: utf-8
import subprocess
from time import sleep


# Windowsの電卓を開く
proc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')

# pollをコールした地点でNoneが返ってくると、プログラム実行中
# 手動でプログラムを終了する場合に値を監視しておくと便利
if proc.poll() is None:
    # 特に待たない
    print("Main End")
