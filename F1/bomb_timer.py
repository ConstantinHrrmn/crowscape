import constants

sev_seg.begin()

    hour = 0
    minute = 5
    second = 0

    base_second = 59

  while(True):


    sev_seg.clear()
    # Set hours
    sev_seg.set_digit(0, int(hour / 10))     # Tens
    sev_seg.set_digit(1, hour % 10)          # Ones
    # Set minutes
    sev_seg.set_digit(2, int(minute / 10))   # Tens
    sev_seg.set_digit(3, minute % 10)        # Ones
    # Toggle colon
    sev_seg.set_colon(second % 2)              # Toggle colon at 1Hz

    second -= 1

    if(second < 0):
        second = base_second
        minute -= 1


    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    sev_seg.write_display()

    # Wait a quarter second (less than 1 second to prevent colon blinking getting$
    time.sleep(1)