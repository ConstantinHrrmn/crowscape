#!/usr/bin/python3

from multiprocessing import Process
import Timer
import main

p = Process(target=Timer.StartTimer,)
p2 = Process(target=main.F5,)
p.start()
p2.start()
p2.join()
p.join()
