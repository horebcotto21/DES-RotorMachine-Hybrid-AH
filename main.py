import time
from RotorMachine import RotorMachine, list_of_rotors
 
rotor = RotorMachine(list_of_rotors, "CAB")
messages = ["HOPE", "HELLO", "NEW YEAR"]
 
print("Rotor Machine")
for message in messages:
    start = time.perf_counter()
    for i in range(1000):
        encrypted = rotor.encrypt(message, "CAB")
        rotor.decrypt(encrypted, "CAB")
    end = time.perf_counter()
    print(" ", message, "time (ms):", round((end - start) / 1000 * 1000, 4))
 
# TODO DES: same as above, using DES
# TODO Hybrid: same as above, rotor machine + DES