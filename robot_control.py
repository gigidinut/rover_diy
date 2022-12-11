import time
from machine import Pin, PWM, I2C, sleep
from ui_html import web_page
try:
    import usocket as socket
except:
    import socket

AIN1 = Pin(22, Pin.OUT)
AIN2 = Pin(23, Pin.OUT)
BIN1 = Pin(21, Pin.OUT)
BIN2 = Pin(19, Pin.OUT)

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
        #check if log is being written (0/1) and the state of the rover (enabled/disabled)
        print('Writing: '+str(writing)+'  State: '+state)
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
              conn.sendall(response)
              conn.close()
              return writing
              break
          else:
              print('Disabling movement')
              response = web_page(state,writing)
              conn.send('HTTP/1.1 200 OK\n')
              conn.send('Content-Type: text/html\n')
              conn.send('Connection: close\n\n')
              conn.sendall(response)
              conn.close()
              return writing
              break
        
        #call and update web UI
        response = web_page(state,writing)
        #send data to socket
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

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

# MAIN LOOP
while True:
    #create connection to the server and print the details
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    #receive up to 1024 bytes
    request = str(conn.recv(1024))
    print('Content = %s' % request)
    #assign url substrings to each command
    enable = request.find('/?enable')
    start_rec = request.find('/?start_rec')
    
    print('STATE is: '+state)
    #check url for the specific commands of each button
    if start_rec == 6:
        writing = 1
        print ('Data recording enabled')
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
    conn.sendall(response)
    conn.close()
