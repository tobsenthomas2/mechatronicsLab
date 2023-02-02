
import pyb, time
from encoder_reader import EncoderClass
from  motor_driver import MotorDriver



if __name__ == "__main__":
    Motor1=MotorDriver(pyb.Pin.board.PA10,pyb.Pin.board.PB4,pyb.Pin.board.PB5,3)
    Motor1.set_duty_cycle(-90)
    encoder=EncoderClass(pyb. Pin.board. PB6,pyb. Pin.board. PB7,4)
    while(1):
         encoder.read()
         time.sleep(0.1)
    