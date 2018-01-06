from threading import (Event, Thread)
import time

def run():
    """
    run: thread running
    """
    print('running')
    while True:
        time.sleep(11)
        break
    print('end run')

if __name__ == '__main__':
    t = Thread(target=run)
    t.start()

    Event().wait(timeout=10)
    print('current end')

    Event().clear()