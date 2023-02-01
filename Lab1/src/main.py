

import encoderClassTobi
import motorDriverClassTobi



if __name__ == "__main__":
    """!
        This is our main, from here we can call MotorDriver() and EncoderClass()
        classes and specify the specific parameters based on what pins we are 
        using.
        From EncoderClass() we call: In1pin and In2pin to define the pins (B6/B7 or C6/C7). 
        And the TimerNR for the timer channel based on the In pins (TCh 4 or 8)
        From MotorDriver() we call: the pin to enable to motor (EN_Pin)
        and set the torque control pins (PB4/5 or PA0/1) as well as the corresponding
        timer (3 or 5)
        We can also call the set_duty_cycle() class to set a specific duty cycle that will
        run the motor in the correct direction at a specific speed
        """
    Motor1=MotorDriver(pyb.Pin.board.PA10,pyb.Pin.board.PB4,pyb.Pin.board.PB5,3)
    Motor1.set_duty_cycle(90)
    encoder=EncoderClass(pyb.Pin.board.PB6,pyb.Pin.board.PB7,4)
    while(1):
         encoder.read()
         time.sleep(0.5)
    