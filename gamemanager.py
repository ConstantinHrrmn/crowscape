#!/usr/bin/python3

from multiprocessing import Process

import Timer
import main

p1 = Process(target=Timer.Start,)
print("The Game Started")
print("---------------------")

p2 = Process(target=main.Start,)


p1.start()
p2.start()

playing = True

while playing:
    
    if(p1.is_alive() is False):
        print("THE BOMB EXPLODED")
        p1.terminate()
        p2.terminate()
        playing = False
        
    if(p2.is_alive() is False):
        print("YOU WIN")
        p1.terminate()
        p2.terminate()
        playing = False
        
    
print("END OF GAME")
