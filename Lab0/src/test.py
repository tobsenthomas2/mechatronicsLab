import pyb
import time

pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
pinA0.high ()
pinA0.low ()