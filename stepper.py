#RPi.GPIO this way i dont understand why everyone does GPIO. shift pi for the register
# time is time duh
import RPi.GPIO as io
import shiftpi.shiftpi as reg
import time

#Setup of the pins BCM mode and turn off them damn warnings
io.setmode(io.BCM)
io.setwarnings(False)
reg.pinsSetup(**{"ser": 4, "rclk": 5, "srclk": 6}) 
# motors
Step = 8
motor1 = range(0, Step)
motor2 = range(0, Step)
both = range(0, Step)
motor1[0] = [0,1,1,1,0,0,0,0]
motor1[1] = [0,0,1,1,0,0,0,0]
motor1[2] = [1,0,1,1,0,0,0,0]
motor1[3] = [1,0,0,1,0,0,0,0]
motor1[4] = [1,1,0,1,0,0,0,0]
motor1[5] = [1,1,0,0,0,0,0,0]
motor1[6] = [1,1,1,0,0,0,0,0]
motor1[7] = [0,1,1,0,0,0,0,0]
motor2[0] = [0,0,0,0,0,1,1,1]
motor2[1] = [0,0,0,0,0,0,1,1]
motor2[2] = [0,0,0,0,1,0,1,1]
motor2[3] = [0,0,0,0,1,0,0,1]
motor2[4] = [0,0,0,0,1,1,0,1]
motor2[5] = [0,0,0,0,1,1,0,0]
motor2[6] = [0,0,0,0,1,1,1,0]
motor2[7] = [0,0,0,0,0,1,1,0]
both[0] = [0,1,1,1,0,1,1,1]
both[1] = [0,0,1,1,0,0,1,1]
both[2] = [1,0,1,1,1,0,1,1]
both[3] = [1,0,0,1,1,0,0,1]
both[4] = [1,1,0,1,1,1,0,1]
both[5] = [1,1,0,0,1,1,0,0]
both[6] = [1,1,1,0,1,1,1,0]
both[7] = [0,1,1,0,0,1,1,0]

def setStep(w1, w2, w3, w4, w5, w6, w7, w8):
	reg.digitalWrite(1, reg.w1)
	reg.digitalWrite(2, reg.w2)
	reg.digitalWrite(3, reg.w3)
	reg.digitalWrite(4, reg.w4)
	reg.digitalWrite(5, reg.w5)
	reg.digitalWrite(6, reg.w6)
	reg.digitalWrite(7, reg.w7)
	reg.digitalWrite(8, reg.w8)

def forward1(delay, steps):
	for i in range(steps):
		for j in range(StepCount):
			setStep(motor1[j][0], motor1[j][1], motor1[j][2], motor1[j][3], motor1[j][4], motor1[j][5], motor1[j][6], motor1[j][7])
			time.sleep(delay)

def forward2(delay, steps):
	for i in range(steps):
		for j in range(StepCount):
			setStep(motor2[j][0], motor2[j][1], motor2[j][2], motor2[j][3], motor2[j][4], motor2[j][5], motor2[j][6], motor2[j][7])
			time.sleep(delay)

def bothforward(delay, steps):
	for i in range(steps):
		for j in range(StepCount):
			setStep(both[j][0], both[j][1], both[j][2], both[j][3], both[j][4], both[j][5], both[j][6], both[j][7])
			time.sleep(delay)
 
def backward1(delay, steps):
	for j in reversed(range(StepCount)):
		for j in range(StepCount):
			setStep(motor1[j][0], motor1[j][1], motor1[j][2], motor1[j][3], motor1[j][4], motor1[j][5], motor1[j][6], motor1[j][7])
			time.sleep(delay)

def backward2(delay, steps):
	for i in range(steps):
		for j in reversed(range(StepCount)):
			setStep(motor2[j][0], motor2[j][1], motor2[j][2], motor2[j][3], motor2[j][4], motor2[j][5], motor2[j][6], motor2[j][7])
			time.sleep(delay)

def bothbackward(delay, steps):
	for i in range(steps):
		for j in reversed(range(StepCount)):
			setStep(both[j][0], both[j][1], both[j][2], both[j][3], both[j][4], both[j][5], both[j][6], both[j][7])
			time.sleep(delay)

def GetSpeed():
	if motorspeed == 'FULL' or 'F':
		delay = 1
	elif motorspeed == 'HALF' or 'H':
		delay == 5
	elif motorspeed == 'SLOW' or 'S':
		delay == 10
	else:
		print ("Invalid Speed")

def GetDir1():
	if direction == 'F' or 'FOWARD':
		forward1(int(delay) / 1000.0, int(steps = steps * 512))
	elif direction == 'B' or 'BACKWARD':
		backward1(int(delay) / 1000.0, int(steps = steps * 512))
	else:
		print("Invalid Direction on 1")

def GetDir2():
	if direction == 'F' or 'FOWARD':
		forward2(int(delay) / 1000.0, int(steps = steps * 512))
	elif direction =='B' or 'BACKWARD':
		backward2(int(delay) / 1000.0, int(steps = steps * 512))
	else:
		print("Invalid Direction on 2")

def GetDir():

	if direction == 'F' or 'FOWARD':
		bothforward(int(delay) / 1000.0, int(steps = steps * 512))
	elif direction == 'B' or 'BACKWARD':
		bothbackward(int(delay) / 1000.0, int(steps = steps * 512))
	else:
		print("Invalid Direction on both")

if __name__ == '__main__':
	while True:
		motor = raw_input("Which Motor? (1, 2, both, or q to exit)").upper()
		direction = raw_input("Forward or Backward?)").upper()
		motorspeed = raw_input("How fast? (full, half, slow)").upper()
		steps = raw_input("How many rotations?")
		print motor
		print direction
		print motorspeed
		print steps
		if motor == 1:
			GetSpeed()
			GetDir1()
		if motor == 2:
			GetSpeed()
			GetDir2()
		if motor == 'BOTH':
			GetSpeed()
			GetDir()
		else:
			print("Invalid Motor")
		if motor == 'Q' or 'QUIT' or 'EXIT':
			print("thanks for playing!!")
			io.cleanup()
			break
