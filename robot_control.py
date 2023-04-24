import time
from machine import Pin, PWM, I2C, sleep
from ui_html import web_page
try:
    import usocket as socket
except:
    import socket
# set pins for dc motors control
AIN1 = Pin(18, Pin.OUT)
AIN2 = Pin(23, Pin.OUT)
BIN1 = Pin(17, Pin.OUT)
BIN2 = Pin(19, Pin.OUT)

# set LED with pin for confirming there is a connection active
LED = Pin(16, Pin.OUT)

# set the servo bits
# I2C setup
i2c = I2C(scl=Pin(22), sda=Pin(21))

# PCA9685 constants
PCA9685_ADDR = 0x40
MODE1_REG = 0x00
PRESCALE_REG = 0xFE
LED0_ON_L_REG = 0x06

# PCA9685 initialization
i2c.writeto_mem(PCA9685_ADDR, MODE1_REG, b'\x10') # Set SLEEP bit to enter sleep mode
i2c.writeto_mem(PCA9685_ADDR, PRESCALE_REG, b'\x79') # Set prescaler to generate 50Hz PWM signal
i2c.writeto_mem(PCA9685_ADDR, MODE1_REG, b'\xA1') # Clear SLEEP bit to enter normal mode
time.sleep_ms(50) # Wait for oscillator to stabilize

# Servo motor control
SERVO_FREQ = 50 # Hz
SERVO_MIN_US = 30 # us
SERVO_MAX_US = 163 # us
SERVO_RANGE_US = SERVO_MAX_US - SERVO_MIN_US
SERVO_CHANNEL = 3
MIN_ANGLE = 0
MAX_ANGLE = 180

# dict storing the current angle of each servo, servoId is the key and angle is the value
servo_angles_dict = {0: 90, 1: 90, 2: 90, 3: 90, 4: 90}

# define rover movement functions
def stop_movement():
    print('Stop')
    AIN1.value(0)
    AIN2.value(0)
    BIN1.value(0)
    BIN2.value(0)

def button_stop_movement():
    #this is called when the a button stops being pressed/clicked and thus I don't want it to print anything
    AIN1.value(0)
    AIN2.value(0)
    BIN1.value(0)
    BIN2.value(0)
  
def move_forward():
    print('Moving forward')
    AIN1.value(1)
    AIN2.value(0)
    BIN1.value(1)
    BIN2.value(0)

def move_backward():
    print('Moving backward')
    AIN1.value(0)
    AIN2.value(1)
    BIN1.value(0)
    BIN2.value(1)
  
def turn_left():
    print('Turning left')
    AIN1.value(1)
    AIN2.value(0)
    BIN1.value(0)
    BIN2.value(1)
  
def turn_right():
    print('Turning right')
    AIN1.value(0)
    AIN2.value(1)
    BIN1.value(1)
    BIN2.value(0)

def robot_movement(writing,state):
    while True:
        #check if in this function without movement enabled and exit if so
        if state != 'ENABLED':
            return writing
            break
        #create connection to the server
        conn, addr = s.accept()
        #receive up to 1024 bytes
        request = str(conn.recv(1024))
        #assign url substrings to each command
        forward = request.find('/?forward')
        backward = request.find('/?backward')
        left = request.find('/?left')
        right = request.find('/?right')
        stop = request.find('/?stop')
        buttonstop = request.find('/?buttonstop')
        stop_rec = request.find('/?stop_rec')
        disable = request.find('/?disable')
        arm_controls = request.find('/?arm_controls')
        #check if log is being written (0/1) and the state of the rover (enabled/disabled)
        #print('Writing: '+str(writing)+'  State: '+state)
        if arm_controls == 6:
            print ('Controling Arm')
            robot_arm_controls(writing,state)
        #check url for the specific commands of each button
        #execute the associated move and record it in the log is writing is enabled
        if forward == 6:
          move_forward()
          if writing == 1:
              f.write(str((time.ticks_ms()-the_time)/1000))
              f.write(',Forward\n')
        if backward == 6:
          move_backward()
          if writing == 1:
              f.write(str((time.ticks_ms()-the_time)/1000))
              f.write(',Backward\n')
        if left == 6:
          turn_left()
          if writing == 1:
              f.write(str((time.ticks_ms()-the_time)/1000))
              f.write(',Left\n')
        if right == 6:
          turn_right()
          if writing == 1:
              f.write(str((time.ticks_ms()-the_time)/1000))
              f.write(',Right\n')
        if stop == 6:
          stop_movement()
          if writing == 1:
              f.write(str((time.ticks_ms()-the_time)/1000))
              f.write(',Stop\n')
        if buttonstop == 6:
            print('button stop')
            button_stop_movement()
            #choosing not to write this to the log as it is called when the button stops being pressed so not really a new action
        if stop_rec == 6:
          if writing == 1:
              f.close()
              print('Recording stopped')
              writing = 0
        if disable == 6:
          if writing == 1:
              f.close()
              print('Recording stopped')
              writing = 0
              print('Disabling movement')
              state = 'DISABLED'
              response = web_page(state,writing)
              conn.send('HTTP/1.1 200 OK\n')
              conn.send('Content-Type: text/html\n')
              conn.send('Connection: close\n\n')
              try:
                  conn.sendall(response)
              except:
                  print('Writing: ' + str(writing) + '    State: ' + state)
                  print("ERROR: Something went wrong - When Disabling, Writing is 1")
              conn.close()
              return writing
              break
          else:
              print('Disabling movement')
              response = web_page(state,writing)
              conn.send('HTTP/1.1 200 OK\n')
              conn.send('Content-Type: text/html\n')
              conn.send('Connection: close\n\n')
              try:
                  conn.sendall(response)
              except:
                  print('Writing: ' + str(writing) + '    State: ' + state)
                  print("ERROR: Something went wrong - When Disabling, Writing is 0")
              conn.close()
              return writing
              break
        
        #call and update web UI
        response = web_page(state,writing)
        #send data to socket
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        try:
            conn.sendall(response)
        except:
            print('Writing: ' + str(writing) + '    State: ' + state)
            print("ERROR: Something went wrong - Inside movement loop")
        conn.close()

def robot_arm_controls(writing,state):
    while True:
        conn, addr = s.accept()
         # receive data from the client
        data = conn.recv(1024)
        if not data:
            conn.close()
            continue
        
        tracks_control = request.find('/?tracks_control')
        
        if tracks_control == 6:
            robot_movement(writing,state)
        
        # parse the data to get the value from the text box
        data_str = str(data, 'utf-8')
        textbox_value = data_str.split('\r\n')[-1].split('=')[-1]
        #print ('texbox_value = ' + textbox_value)
        
        try:
            # split value sent into input id and angle value
            inputId, angle = textbox_value.split('#', 1)
            # convert string to int for angle
            angle = int(angle)
            # set value of servo id for the controller board
            if inputId == 'input1':
                servoId = 0 # base servo - horizontal movemenet
            elif inputId == 'input2':
                servoId = 1 # base servo 2 - first vertical joint
            elif inputId == 'input3':
                servoId = 2 # servo 3 - 2nd vertical join / elbow
            elif inputId == 'input4':
                servoId = 3 # servo 4 - 3rd vertical joint / wrist
            elif inputId == 'input5':
                servoId = 4 # servo 5 - claw
            
            # do something with the textbox value
            angle2 = str(angle)
            #print('Servo number: ' + inputId + '  // Angle: ' + angle2)
        except:
            print ('There was nothing passed to the arm')
            break
        
        # extract current angle value for the servo from the dict
        current_angle = servo_angles_dict[servoId]
        
        new_angle = angle
        
        # call the servo_control function to control the individual servos
        new_current_angle = servo_control (servoId, current_angle, new_angle)
        
        # put the angle for the specific servo into the dict
        servo_angles_dict[servoId] = new_current_angle
        
        #call and update web UI
        response = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n<html><body><h1>Textbox value: %s</h1></body></html>' % textbox_value
        #send data to socket
        conn.send(response.encode())
        try:
            conn.sendall(response)
        except:
            print('Writing: ' + str(writing) + '    State: ' + state)
            print("ERROR: Something went wrong - Inside arm loop")
        conn.close()

def servo_control (servoId, current_angle, new_angle):
    SERVO_FREQ = 50 # Hz
    SERVO_MIN_US = 30 # us
    SERVO_MAX_US = 163 # us
    SERVO_RANGE_US = SERVO_MAX_US - SERVO_MIN_US
    SERVO_CHANNEL = servoId

    if new_angle > current_angle:
        for angle in range(current_angle, new_angle, 2):
            # Convert angle to PWM duty cycle
            duty_us = int(SERVO_MIN_US + (angle / 180) * SERVO_RANGE_US)
            #duty_us = int(SERVO_MAX_US - (angle / 180) * SERVO_RANGE_US)
            #print('duty_us = ', duty_us)
            duty_val = int(duty_us * SERVO_FREQ * 0x10000 / 1000000)
            # Write duty cycle to PCA9685
            i2c.writeto_mem(PCA9685_ADDR, LED0_ON_L_REG + SERVO_CHANNEL * 4, bytes([0, 0, duty_val & 0xFF, duty_val >> 8]))
        
            time.sleep_ms(20)
    
    if new_angle < current_angle:
        for angle in range(current_angle, new_angle, -2):
            # Convert angle to PWM duty cycle
            duty_us = int(SERVO_MIN_US + (angle / 180) * SERVO_RANGE_US)
            #duty_us = int(SERVO_MAX_US - (angle / 180) * SERVO_RANGE_US)
            #print('duty_us = ', duty_us)
            duty_val = int(duty_us * SERVO_FREQ * 0x10000 / 1000000)
            # Write duty cycle to PCA9685
            i2c.writeto_mem(PCA9685_ADDR, LED0_ON_L_REG + SERVO_CHANNEL * 4, bytes([0, 0, duty_val & 0xFF, duty_val >> 8]))
            
            time.sleep_ms(20)
    
    # atribute the new angle to the current angle
    current_angle = new_angle
    
    return current_angle

#create new socket and listen for incoming connections on port 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
#queue up to 5 connections before refusing new ones
s.listen(5)

#open the log file by default
#the log records the time in seconds since the program started running and the action being performed - from the button press
f = open('movementlog.txt', 'w')
the_time = time.ticks_ms()
f.write('Time(ms),Action\n')
#default state is disabled and log not recording
writing = 0
state = 'DISABLED'

error_counter = 0

# MAIN LOOP
while True:
    #create connection to the server and print the details
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    #receive up to 1024 bytes
    request = str(conn.recv(1024))
    #print('Content = %s' % request)
    #assign url substrings to each command
    enable = request.find('/?enable')
    start_rec = request.find('/?start_rec')
    arm_controls = request.find('/?arm_controls')
    
    print('STATE is: '+state)
    #check url for the specific commands of each button
    if start_rec == 6:
        writing = 1
        print ('Data recording enabled')
    if arm_controls == 6:
        print ('Controling Arm')
        robot_arm_controls(writing,state)
    if enable == 6:
        print('Enabling movement')
        state = 'ENABLED'
        writing = robot_movement(writing,state)
        print('robot_movement returned: ' + str(writing))
        state = 'DISABLED'
    #call and update web UI
    response = web_page(state,writing)
    #send data to socket
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    try:
        conn.sendall(response)
    except:
        print('Writing: ' + str(writing) + '    State: ' + state)
        print("ERROR: Something went wrong - Inside main loop")
        error_counter = error_counter + 1
        print(str(error_counter))
    conn.close()

