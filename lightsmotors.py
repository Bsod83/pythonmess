#shiftpi import this way is important
import shiftpi.shiftpi as shiftpi
import time

#LIGHTS PINS ser 4,rclk 5,srclk 6
#MOTOR PINS ser 24,rclk 25,srclk 26
#CHAGE AT build/lib.linux-armv6l-2.7/shiftpi 
shiftpi.pinsSetup(**{"ser": 4, "rclk": 5, "srclk": 6})
def spin(motor, sec):
	ticks = sec * 1000
	if motor == 1:
		shiftpi.digitalWrite(1, shiftpi.HIGH)
		shiftpi.delay(50)
		shiftpi.digitalWrite(2, shiftpi.HIGH)
		shiftpi.delay(50)
		shiftpi.digitalWrite(1, shiftpi.LOW)
		shiftpi.delay(50)
		shiftpi.digitalWrite(3, shiftpi.HIGH)
		shiftpi.delay(50)
		shiftpi.digitalWrite(2, shiftpi.LOW)
		shiftpi.delay(50)
		shiftpi.digitalWrite(4, shiftpi.HIGH)
		shiftpi.delay(50)
		shiftpi.digitalWrite(3, shiftpi.LOW)
		shiftpi.delay(50)
		shiftpi.digitalWrite(1, shiftpi.HIGH)
		shiftpi.delay(50)
		shiftpi.digitalWrite(4, shiftpi.LOW)
		shiftpi.delay(50)
		ticks=ticks-750
		
		shiftpi.digitalWrite(1, shiftpi.LOW)
		shiftpi.digitalWrite(2, shiftpi.LOW)
		shiftpi.digitalWrite(3, shiftpi.LOW)
		shiftpi.digitalWrite(4, shiftpi.LOW)

	else:
		if motor == 2:
			shiftpi.digitalWrite(5, shiftpi.HIGH)
			shiftpi.digitalWrite(6, shiftpi.HIGH)
			shiftpi.digitalWrite(7, shiftpi.HIGH)
			shiftpi.digitalWrite(8, shiftpi.HIGH)
			shiftpi.delay(ticks)
			shiftpi.digitalWrite(5, shiftpi.LOW)
			shiftpi.digitalWrite(6, shiftpi.LOW)
			shiftpi.digitalWrite(7, shiftpi.LOW)
			shiftpi.digitalWrite(8, shiftpi.LOW)
		else:
			if motor == 3:
				shiftpi.digitalWrite(1, shiftpi.HIGH)
				shiftpi.digitalWrite(2, shiftpi.HIGH)
				shiftpi.digitalWrite(3, shiftpi.HIGH)
				shiftpi.digitalWrite(4, shiftpi.HIGH)
				shiftpi.digitalWrite(5, shiftpi.HIGH)
				shiftpi.digitalWrite(6, shiftpi.HIGH)
				shiftpi.digitalWrite(7, shiftpi.HIGH)
				shiftpi.digitalWrite(8, shiftpi.HIGH)
				shiftpi.delay(ticks)
				shiftpi.digitalWrite(1, shiftpi.LOW)
				shiftpi.digitalWrite(2, shiftpi.LOW)
				shiftpi.digitalWrite(3, shiftpi.LOW)
				shiftpi.digitalWrite(4, shiftpi.LOW)
				shiftpi.digitalWrite(5, shiftpi.LOW)
				shiftpi.digitalWrite(6, shiftpi.LOW)
				shiftpi.digitalWrite(7, shiftpi.LOW)
				shiftpi.digitalWrite(8, shiftpi.LOW)
			else:
				shiftpi.digitalWrite(1, shiftpi.LOW)
				shiftpi.digitalWrite(2, shiftpi.LOW)
				shiftpi.digitalWrite(3, shiftpi.LOW)
				shiftpi.digitalWrite(4, shiftpi.LOW)
				shiftpi.digitalWrite(5, shiftpi.LOW)
				shiftpi.digitalWrite(6, shiftpi.LOW)
				shiftpi.digitalWrite(7, shiftpi.LOW)
				shiftpi.digitalWrite(8, shiftpi.LOW)
	return 1
def main():
	spin(1,1)
	spin(2,1)
	spin(3,1)
	return 1
main()
