#!/usr/bin/python3

from multiprocessing import Process
import Timer
import main

import os

p = Process(target=Timer.Start,)
p2 = Process(target=main.Start,)

p.start()
p2.start()

print(p.pid)
print(p2.pid)

p2.join()
p.join()

