import threading
import time
from time import perf_counter
import psutil

from RotorMachine import RotorMachine, list_of_rotors
from DES import DES

cpu_samples = []
stop_flag = False

def monitor_cpu():
    while not stop_flag:
        cpu_samples.append(psutil.cpu_percent(interval=0.5))
 
rotor = RotorMachine(list_of_rotors, "CAB")
messages = ["HOPE", "HELLO", "NEW YEAR"]


print("Rotor Machine")
for message in messages:
    start = time.perf_counter()
    stop_flag = False
    t = threading.Thread(target=monitor_cpu)
    t.start()
    for i in range(1000):
        encrypted = rotor.encrypt(message, "CAB")
        rotor.decrypt(encrypted, "CAB")
    end = time.perf_counter()
    cpu_util_end =  perf_counter()
    stop_flag = True
    t.join()
    print(" ", message, "time (ms):", round((end - start) / 1000 * 1000, 4))
    print("Avg CPU %:", f"{sum(cpu_samples) / len(cpu_samples):3f}\n")
# TODO DES: same as above, using DES
print("DES algorithm")
for message in messages:
    start = time.perf_counter()
    stop_flag = False
    t = threading.Thread(target=monitor_cpu)
    t.start()
    for i in range(1000):
        encrypted = DES("1337BACEF18CC54D").encrypt(message)
        DES("1337BACEF18CC54D").decrypt(encrypted)
    end = time.perf_counter()
    cpu_util_end = perf_counter()
    stop_flag = True
    t.join()
    print(" ", message, "time (ms):", round((end - start) / 1000 * 1000, 4))
    print("Avg CPU %:", f"{sum(cpu_samples) / len(cpu_samples):3f}\n")
# TODO Hybrid: same as above, rotor machine + DES
