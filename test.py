import os
import time

print("hello")
time.sleep(10)
if os.name == "nt":
    os.system('cls')
else:
    os.system('clear')


