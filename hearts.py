# import the things
import shiftpi.shiftpi as sp
# Number of 595n
# 1-32 2 lights per bit 
# 33 37 41 45 single lights
# 34-36 38-40 42-44 46-48 rgb lights
sp.shiftRegisters(6)
# lights go up and down either side of hearts
# ========================= #
  def slide():
    sp.digitalWrite(1, sp.HIGH)
    sp.digitalWrite(8, sp.HIGH)
    sp.digitalWrite(17, sp.HIGH)
    sp.digitalWrite(25, sp.HIGH)
    sp.delay(75)
    sp.digitalWrite(2, sp.HIGH)
    sp.digitalWrite(9, sp.HIGH)
    sp.digitalWrite(18, sp.HIGH)
    sp.digitalWrite(26, sp.HIGH)
    sp.delay(75)
    sp.digitalWrite(1, sp.LOW)
    sp.digitalWrite(8, sp.LOW)
    sp.digitalWrite(17, sp.LOW)
    sp.digitalWrite(25, sp.LOW)
    sp.delay(75)
    sp.digitalWrite(3, sp.HIGH)
    sp.digitalWrite(10, sp.HIGH)
    sp.digitalWrite(19, sp.HIGH)
    sp.digitalWrite(27, sp.HIGH)
    sp.delay(75)
    sp.digitalWrite(2, sp.LOW)
    sp.digitalWrite(9, sp.LOW)
    sp.digitalWrite(18, sp.LOW)
    sp.digitalWrite(26, sp.LOW)
    sp.delay(75)
    sp.digitalWrite(4, sp.HIGH)
    sp.digitalWrite(11, sp.HIGH)
    sp.digitalWrite(20, sp.HIGH)
    sp.digitalWrite(28, sp.HIGH)
    sp.delay(75)
    sp.digitalWrite(3, sp.LOW)
    sp.digitalWrite(10, sp.LOW)
    sp.digitalWrite(19, sp.LOW)
    sp.digitalWrite(27, sp.LOW)
    sp.delay(75)
    sp.digitalWrite(5, sp.HIGH)
    sp.digitalWrite(12, sp.HIGH)
    sp.digitalWrite(21, sp.HIGH)
    sp.digitalWrite(29, sp.HIGH)
    sp.delay(75)
    sp.digitalWrite(4, sp.LOW)
    sp.digitalWrite(11, sp.LOW)
    sp.digitalWrite(20, sp.LOW)
    sp.digitalWrite(28, sp.LOW)
    sp.delay(75)
    sp.digitalWrite(6, sp.HIGH)
    sp.digitalWrite(13, sp.HIGH)
    sp.digitalWrite(22, sp.HIGH)
    sp.digitalWrite(30, sp.HIGH)
    sp.delay(75)
    sp.digitalWrite(5, sp.LOW)
    sp.digitalWrite(12, sp.LOW)
    sp.digitalWrite(21, sp.LOW)
    sp.digitalWrite(29, sp.LOW)
    sp.delay(75)
    sp.digitalWrite(7, sp.HIGH)
    sp.digitalWrite(14, sp.HIGH)
    sp.digitalWrite(23, sp.HIGH)
    sp.digitalWrite(31, sp.HIGH)
    sp.delay(75)
    sp.digitalWrite(6, sp.LOW)
    sp.digitalWrite(13, sp.LOW)
    sp.digitalWrite(22, sp.LOW)
    sp.digitalWrite(30, sp.LOW)
    sp.delay(75)
    sp.digitalWrite(8, sp.HIGH)
    sp.digitalWrite(15, sp.HIGH)
    sp.digitalWrite(24, sp.HIGH)
    sp.digitalWrite(32, sp.HIGH)
    sp.delay(75)
    sp.digitalWrite(7, sp.LOW)
    sp.digitalWrite(14, sp.LOW)
    sp.digitalWrite(23, sp.LOW)
    sp.digitalWrite(31, sp.LOW)
    sp.delay(75)
    sp.digitalWrite(8, sp.LOW)
    sp.digitalWrite(15, sp.LOW)
    sp.digitalWrite(24, sp.LOW)
    sp.digitalWrite(32, sp.LOW)
    sp.delay(75)
#===============#
# Blink all the lights
  def blink():
    sp.digitalWrite(1, sp.HIGH)
    sp.digitalWrite(2, sp.HIGH)
    sp.digitalWrite(3, sp.HIGH)
    sp.digitalWrite(4, sp.HIGH)
    sp.digitalWrite(5, sp.HIGH)
    sp.digitalWrite(6, sp.HIGH)
    sp.digitalWrite(7, sp.HIGH)
    sp.digitalWrite(8, sp.HIGH)
    sp.digitalWrite(9, sp.HIGH)
    sp.digitalWrite(10, sp.HIGH)
    sp.digitalWrite(11, sp.HIGH)
    sp.digitalWrite(12, sp.HIGH)
    sp.digitalWrite(13, sp.HIGH)
    sp.digitalWrite(14, sp.HIGH)
    sp.digitalWrite(15, sp.HIGH)
    sp.digitalWrite(16, sp.HIGH)
    sp.digitalWrite(17, sp.HIGH)
    sp.digitalWrite(18, sp.HIGH)
    sp.digitalWrite(19, sp.HIGH)
    sp.digitalWrite(20, sp.HIGH)
    sp.digitalWrite(21, sp.HIGH)
    sp.digitalWrite(22, sp.HIGH)
    sp.digitalWrite(23, sp.HIGH)
    sp.digitalWrite(24, sp.HIGH)
    sp.digitalWrite(25, sp.HIGH)
    sp.digitalWrite(26, sp.HIGH)
    sp.digitalWrite(27, sp.HIGH)
    sp.digitalWrite(28, sp.HIGH)
    sp.digitalWrite(29, sp.HIGH)
    sp.digitalWrite(30, sp.HIGH)
    sp.digitalWrite(31, sp.HIGH)
    sp.digitalWrite(32, sp.HIGH)
    sp.digitalWrite(1, sp.LOW)
    sp.digitalWrite(2, sp.LOW)
    sp.digitalWrite(3, sp.LOW)
    sp.digitalWrite(4, sp.LOW)
    sp.digitalWrite(5, sp.LOW)
    sp.digitalWrite(6, sp.LOW)
    sp.digitalWrite(7, sp.LOW)
    sp.digitalWrite(8, sp.LOW)
    sp.digitalWrite(9, sp.LOW)
    sp.digitalWrite(10, sp.LOW)
    sp.digitalWrite(11, sp.LOW)
    sp.digitalWrite(12, sp.LOW)
    sp.digitalWrite(13, sp.LOW)
    sp.digitalWrite(14, sp.LOW)
    sp.digitalWrite(15, sp.LOW)
    sp.digitalWrite(16, sp.LOW)
    sp.digitalWrite(17, sp.LOW)
    sp.digitalWrite(18, sp.LOW)
    sp.digitalWrite(19, sp.LOW)
    sp.digitalWrite(20, sp.LOW)
    sp.digitalWrite(21, sp.LOW)
    sp.digitalWrite(22, sp.LOW)
    sp.digitalWrite(23, sp.LOW)
    sp.digitalWrite(24, sp.LOW)
    sp.digitalWrite(25, sp.LOW)
    sp.digitalWrite(26, sp.LOW)
    sp.digitalWrite(27, sp.LOW)
    sp.digitalWrite(28, sp.LOW)
    sp.digitalWrite(29, sp.LOW)
    sp.digitalWrite(30, sp.LOW)
    sp.digitalWrite(31, sp.LOW)
    sp.digitalWrite(32, sp.LOW)
     
#===================#

  def circle():
    sp.digitalWrite(1, sp.HIGH)
    sp.digitalWrite(17, sp.HIGH)
    sp.delay(50)
    sp.digitalWrite(2, sp.HIGH)
    sp.digitalWrite(18, sp.HIGH)
    sp.delay(50)
    sp.digitalWrite(1, sp.LOW)
    sp.digitalWrite(17, sp.LOW)
    sp.delay(50)
    sp.digitalWrite(3, sp.HIGH)
    sp.digitalWrite(19, sp.HIGH)
    sp.delay(50)
    sp.digitalWrite(2, sp.LOW)
    sp.digitalWrite(18, sp.LOW)
    sp.delay(50)
    sp.digitalWrite(2, sp.HIGH)
    sp.digitalWrite(18, sp.HIGH)
    sp.delay(50)
    sp.digitalWrite(1, sp.LOW)
    sp.digitalWrite(17, sp.LOW)
    sp.delay(50)
    sp.digitalWrite(2, sp.High)
    sp.digitalWrite(18, sp.High)
