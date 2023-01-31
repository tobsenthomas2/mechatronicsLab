import pyb
import time

class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several pin parameters)
        """
        self.enable_pin=en_pin
        self.IN1_Pin=in1pin
        self.IN2_Pin=in2pin
        self.pwmTim=timer
       
        
        pinEN = pyb.Pin (self.enable_pin, pyb.Pin.OUT_PP) #enable
        pinEN.value(1)
        
        pinIn1 = pyb.Pin (self.IN1_Pin, pyb.Pin.OUT_PP) 
        pinIn2 = pyb.Pin (self.IN2_Pin, pyb.Pin.OUT_PP) 
        
        tim = pyb.Timer (self.pwmTim, freq=20000)
        
        self.ch1 = tim.channel (1, pyb.Timer.PWM, pin=pinIn1)
        self.ch2 = tim.channel (2, pyb.Timer.PWM, pin=pinIn2)
        
        
        print ("Creating a motor driver")

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
      
        if (level<0):
            self.ch1.pulse_width_percent (abs(level))
            self.ch2.pulse_width_percent (0)
        else:
            self.ch1.pulse_width_percent (0)
            self.ch2.pulse_width_percent (abs(level))
            
        
        print (f"Setting duty cycle to {level}")
#         
# if __name__ == "__main__":
#     Motor1=MotorDriver(pyb.Pin.board.PA10,pyb.Pin.board.PB4,pyb.Pin.board.PB5,3)
#     Motor1.set_duty_cycle(90)
#     Motor2=MotorDriver(pyb.Pin.board.PC1,pyb.Pin.board.PA0,pyb.Pin.board.PA1,5)