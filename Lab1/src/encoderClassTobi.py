# import pyb
# import time


class EncoderClass:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, in1pin, in2pin, timerNR):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several pin parameters)
        """
        self.IN1_Pin=in1pin
        self.IN2_Pin=in2pin
        self.counterTimer=timerNR
        
        
        
        enc_chA = pyb.Pin(self.IN1_Pin, pyb.Pin.IN)

        enc_chB = pyb.Pin (self.IN2_Pin, pyb.Pin.IN)

        timer= pyb.Timer (self.counterTimer, prescaler=0, period=0xFFFF)
        ch1=timer.channel (1, pyb.Timer.ENC_AB, pin=enc_chA)
        ch2=timer.channel (2, pyb.Timer.ENC_AB, pin=enc_chB)
        self.counter=timer
        
        print ("Creating a motor driver")

    def read (self):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        print("counter " +str(self.counter.counter())+" for encoderTim: " +str(self.counterTimer))
        
    def zero(self):
        print("reset counter to 0")
        self.counter.counter(0)
        
        
        
#         
#         
# if __name__ == "__main__":
#     encoder=EncoderClass(pyb. Pin.board. PB6,pyb. Pin.board. PB7,4)
#     while(1):
#          encoder.read()
#          time.sleep(0.5)