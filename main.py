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


print("\n--- Rotor Machine ---")
print("Message".ljust(10), "|", "Encrypted".ljust(10), "|", "Decrypted".ljust(10), "|", "Time (ms)".ljust(10), "|", "CPU %")
print("-" * 62)
for message in messages:
    start = time.perf_counter()
    stop_flag = False
    t = threading.Thread(target=monitor_cpu)
    t.start()
    for i in range(1000):
        encrypted = rotor.encrypt(message, "CAB")
        decrypted = rotor.decrypt(encrypted, "CAB")
    end = time.perf_counter()
    cpu_util_end =  perf_counter()
    stop_flag = True
    t.join()
    time_ms = str(round((end - start) / 1000 * 1000, 4))
    cpu = f"{sum(cpu_samples) / len(cpu_samples):.2f}"
    print(message.ljust(10), "|", encrypted.ljust(10), "|", decrypted.ljust(10), "|", time_ms.ljust(10), "|", cpu)

print("\n--- DES ---")
print("Message".ljust(10), "|", "Encrypted".ljust(18), "|", "Decrypted".ljust(10), "|", "Time (ms)".ljust(10), "|", "CPU %")
print("-" * 70)
for message in messages:
    start = time.perf_counter()
    stop_flag = False
    t = threading.Thread(target=monitor_cpu)
    t.start()
    for i in range(1000):
        encrypted = DES("1337BACEF18CC54D").encrypt(message)
        decrypted = DES("1337BACEF18CC54D").decrypt(encrypted)
    end = time.perf_counter()
    cpu_util_end = perf_counter()
    stop_flag = True
    t.join()
    time_ms = str(round((end - start) / 1000 * 1000, 4))
    cpu = f"{sum(cpu_samples) / len(cpu_samples):.2f}"
    print(message.ljust(10), "|", encrypted.ljust(18), "|", decrypted.ljust(10), "|", time_ms.ljust(10), "|", cpu)

print("\n--- Hybrid Rotor + DES ---")
long_messages = ["HOW ARE YOU", "HAPPY NEW YEAR", "WELCOME TO PUERTO RICO"]
print("Message".ljust(23), "|", "Rotor encrypt".ljust(23), "|", "DES encrypt".ljust(48), "|", "Decrypted".ljust(23), "|", "Time (ms)".ljust(9), "|", "CPU %")
print("-" * 145)

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
    end = time.perf_counter()
    cpu_util_end = perf_counter()
    stop_flag = True
    t.join()
    time_ms = str(round((end - start) / 1000 * 1000, 4))
    cpu = f"{sum(cpu_samples) / len(cpu_samples):.2f}"
    print(message.ljust(23), "|", encrypted.ljust(23), "|", encrypted_2.ljust(48), "|", decrypted_2.ljust(23), "|", time_ms.ljust(9), "|", cpu)