#Motordriver

"""!
Lab0 Documentation 
Team mecha02: Sydney Gothenquist, Toby Moss Darci-Maher, Tobias Thomas 
 
The Program should lead to a dimming LED controlled by a STM32 and written in micropython. 
The LED will be from off to on in 5 secudes and the brighntes will increase every 0.05 secundes
"""

"""! this imports the libraries, pyb and time """
import pyb
import time

def Motor_shield_init ():
    
    
#"""! init function for all Pins.

#This function enables the shield and set up the timer for PWM
#Pin EN PA10 + TIM3 and PC1 + TIM5
 #   """
    
    pinA10 = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP) #enable
    pinB4 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP) #Tim3Ch1
    pinB5 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP) #Tim3Ch2
    
    pinC1 = pyb.Pin (pyb.Pin.board.PC1, pyb.Pin.OUT_PP) #enable
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP) #Tim5Ch1
    pinA1 = pyb.Pin (pyb.Pin.board.PA1, pyb.Pin.OUT_PP) ##Tim5Ch2
    
    tim3 = pyb.Timer (3, freq=20000)
    tim5 = pyb.Timer (5, freq=20000)
    
    
    global ch31
    global ch32
    
    global ch51
    global ch52
    
    ch31 = tim3.channel (1, pyb.Timer.PWM, pin=pinB4)
    ch32 = tim3.channel (2, pyb.Timer.PWM, pin=pinB5)
    
    ch51 = tim5.channel (1, pyb.Timer.PWM, pin=pinA0)
    ch52 = tim5.channel (2, pyb.Timer.PWM, pin=pinA1)
    
    #set enable to high
    pinA10.value(1)
    pinC1.value(1)

def motor_speed ():#Motor,dir,perc):
# """! controll function needs brightness percentage as input
# 
# this function, led_brightness defines the brightness of the led as set by the PWM duty cycle.
# this duty cycle ranges from 0-100%, and is defined by "value" in the main function
#     """

    global ch31
    global ch32
    
    global ch51
    global ch52
    #pyb.Timer.PWM_INVERTED # did not work for us, so we implemented a workaround
    perc=90
    ch31.pulse_width_percent (perc)
    ch32.pulse_width_percent (0)
    
    ch51.pulse_width_percent (perc)
    ch52.pulse_width_percent (0)
    
    ch31.pulse_width_percent (0)
    ch32.pulse_width_percent (perc)
    
    ch51.pulse_width_percent (0)
    ch52.pulse_width_percent (perc)
  
if __name__ == "__main__":
#"""!in this main function, we are running the seperately defined functions, led_setup and led_brightness 
 #   """
    Motor_shield_init()
    time.sleep(1)
#    """! by setting i = 0, this creates an infinite loop so that the LED will keep looping until
 #   the program is stopped since the while loop will only stop if i > 10 """
    
    
    i=0  
    while i<=10:
#     """! sets the value to what is specified and decrements down from 100 to 0, as we did not use the INVERTED function
#         the range for value is set from 0-100 so that it cannot go out of this range.
#         100 = dimmest and 0 = brightest as per the not inverted PWM """
#         
        for  value in range(100,0,-1):
       # """! the led brightness is equivalent to the specified value as defined by the for loop """
            
            motor_speed()
            
#             """! each run through this for loop will be for 0.05s. Since it is running 100x, this equates
#             to a total runtime of 5s as specified in the lab """
            
            time.sleep(0.05)
     