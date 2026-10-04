import multiprocessing
import time
import random
from datetime import datetime

def worker(name):
    delay = random.random()
    time.sleep(delay)

    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Process {name} | finished at {current_time} | after sleeping for {delay:.2f}  | seconds.")

if __name__ == "__main__":
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
