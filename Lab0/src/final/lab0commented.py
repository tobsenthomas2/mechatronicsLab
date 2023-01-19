"""!
Lab0 Documentation 
Team mecha02: Sydney Gothenquist, Toby Moss Darci-Maher, Tobias Thomas 
 
The Program should lead to a dimming LED controlled by a STM32 and written in micropython. 
The LED will be from off to on in 5 secudes and the brighntes will increase every 0.05 secundes
"""

"""! this imports the libraries, pyb and time """
import pyb
import time

def led_setup ():
"""! init function for all Pins.

This function, led_setup, sets up the pins for timer 2, channel 1
the A0 pin functions as an output with input from the 3v3 port for the LED.

    """
    
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer (2, freq=20000)
    
    global ch2
    ch2 = tim2.channel (1, pyb.Timer.PWM, pin=pinA0)

def led_brightness (perc):
"""! controll function needs brightness percentage as input

this function, led_brightness defines the brightness of the led as set by the PWM duty cycle.
this duty cycle ranges from 0-100%, and is defined by "value" in the main function
    """

    global ch2
    #pyb.Timer.PWM_INVERTED # did not work for us, so we implemented a workaround
    ch2.pulse_width_percent (perc)
  
if __name__ == "__main__":
"""!in this main function, we are running the seperately defined functions, led_setup and led_brightness 
    """
    led_setup()
    time.sleep(1)
    """! by setting i = 0, this creates an infinite loop so that the LED will keep looping until
    the program is stopped since the while loop will only stop if i > 10 """
    
    
    i=0  
    while i<=10:
    """! sets the value to what is specified and decrements down from 100 to 0, as we did not use the INVERTED function
        the range for value is set from 0-100 so that it cannot go out of this range.
        100 = dimmest and 0 = brightest as per the not inverted PWM """
        
        for  value in range(100,0,-1):
        """! the led brightness is equivalent to the specified value as defined by the for loop """
            
            led_brightness(value)
            
            """! each run through this for loop will be for 0.05s. Since it is running 100x, this equates
            to a total runtime of 5s as specified in the lab """
            
            time.sleep(0.05)
     