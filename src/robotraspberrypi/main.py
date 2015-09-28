from robotraspiberrypi.robot import robot

def drive():
    return "Not Implemented"

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