#!/usr/bin/python3
from constants import GPIO, sev_seg, time, buzzer
    
def DisplayOnSVG(minute, second):
    sev_seg.clear()
    
    sev_seg.set_digit(0, int(minute / 10))     # Tens
    sev_seg.set_digit(1, minute % 10)          # Ones

    sev_seg.set_digit(2, int(second / 10))   # Tens
    sev_seg.set_digit(3, second % 10)        # Ones
    
    sev_seg.set_colon(second % 2)
    sev_seg.write_display()
      
def Start():
    sev_seg.begin()
    
    minute = 5 # le nombre de minutes avec lequel le minuteur commence
    second = 0 # le nombre de secondes avec lequel le minuteur commence
    base_second = 59 # Les secondes max par défaut
    
    while True:   
        
        DisplayOnSVG(minute, second) 
        
        if(minute <= 0 and second <= 0):
            break
        
        second -= 1
        if(second < 0):
            second = base_second
            minute -= 1
        
        time.sleep(1)
