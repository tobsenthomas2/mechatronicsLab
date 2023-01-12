import pyb
import time

#"""! Doxygen style docstring for the file """

def led_setup ():
 #      """! Doxygen style docstring for this function """
    #pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    #pinA0.high ()
    #pinA0.low ()
    #time.sleep(1)
    
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer (2, freq=20000)
    
    global ch2
    ch2 = tim2.channel (1, pyb.Timer.PWM, pin=pinA0)
    

def led_brightness (perc):
 #      """! Doxygen style docstring for this function """
    
    global ch2
    #pyb.Timer.PWM_INVERTED
    ch2.pulse_width_percent (perc)
    #ch2.pulse_width_percent (50)
    

if __name__ == "__main__":
    led_setup()
    time.sleep(1)
    #led_brightness(20)
    i=0
    while i<=10:
        for  value in range(100,0,-1):
            led_brightness(value)
            time.sleep(0.05)
#     
#     time.sleep(1)
#     led_brightness(100)
#     time.sleep(1)
#     led_brightness(0)
#     time.sleep(1)
#     led_brightness(50)
#     