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
print("DES algorithm\n")
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

print("Hybrid Rotor + DES\n")
long_messages = ["HOW ARE YOU", "HAPPY NEW YEAR", "WELCOME TO PUERTO RICO"]

for message in long_messages:
    start = time.perf_counter()
    stop_flag = False
    t = threading.Thread(target=monitor_cpu)
    t.start()
    for i in range(1000):
        encrypted = rotor.encrypt(message, "CAB")
        encrypted_2 = DES("1337BACEF18CC54D").encrypt(encrypted)
        decrypted = DES("1337BACEF18CC54D").decrypt(encrypted_2)
        decrypted_2 = rotor.decrypt(decrypted, "CAB")

    print("E1: ", encrypted,"-> E2",encrypted_2, "-> D1: ",decrypted,"-> D2: ",decrypted_2)
    end = time.perf_counter()
    cpu_util_end = perf_counter()
    stop_flag = True
    t.join()
    print(" ", message, "time (ms):", round((end - start) / 1000 * 1000, 4))
    print("Avg CPU %:", f"{sum(cpu_samples) / len(cpu_samples):3f}\n")