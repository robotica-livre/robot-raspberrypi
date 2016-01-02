from robot import *

direction = {
    1 : forward,
    2 : left,
    3 : right,
    4 : backward,
} 

def drive(left = 255, right = 255, dir):
    direction[dir](left, right);
    
def forward(left, right):
    robot.set_motors(left, 0, right, 0)

def left(left, right):
    robot.set_motors(left, 1, right, 0)

def right(left, right):
    robot.set_motors(left, 0, right, 1)

def backward(left, right):
    robot.set_motors(left, 1, right, 1)

def line_following():
    Kp = 1 / 20
    Ki = 1 / 10000
    Kd = 3/2
    integral = 0.0
    derivative = 0.0
    prev_error = 0.0 
    
    while(1):
        time.sleep(0.1)
        position = read_sensors()
        
        error = 0.0 - position
        integral = integral + error * 0.1
        derivative = (error - prev_error) / 0.1
        
        power_diff = (Kp * error) + (Ki * integral) + (Kd * derivative)
        prev_error = error
        
        # method used to set motors speed after run PID algorithm
        robot.set_motors(0, 0, 0, 0)
    return "Not yet Implemented"

def read_sensors():
    GPIO.setup(22, GPIO.IN)
    GPIO.setup(23, GPIO.IN)
    GPIO.setup(24, GPIO.IN)
    return "Not implemented"

def robot():
    return "Not Implemented"

if __name__ == "__main__":
    robot()