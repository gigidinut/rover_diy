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
    
def stop_movement():
    print('Stop')
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
        conn, addr = s.accept()
        request = str(conn.recv(1024))
        #print('Content = %s' % request)
        forward = request.find('/?forward')
        backward = request.find('/?backward')
        left = request.find('/?left')
        right = request.find('/?right')
        stop = request.find('/?stop')
        stop_rec = request.find('/?stop_rec')
        disable = request.find('/?disable')
        
        print('Writing: '+str(writing)+'  State: '+state)
        
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
              response = web_page(state)
              conn.send('HTTP/1.1 200 OK\n')
              conn.send('Content-Type: text/html\n')
              conn.send('Connection: close\n\n')
              conn.sendall(response)
              conn.close()
              return writing
              break
          else:
              print('Disabling movement')
              response = web_page(state)
              conn.send('HTTP/1.1 200 OK\n')
              conn.send('Content-Type: text/html\n')
              conn.send('Connection: close\n\n')
              conn.sendall(response)
              conn.close()
              return writing
              break
              
        print('State sent to web page in loop: ' + state)  
        response = web_page(state)
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

#web_page()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

f = open('movementlog.txt', 'w')
the_time = time.ticks_ms()
f.write('Time(ms),Action')
f.write('\n')
writing = 0
state = 'DISABLED'
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = str(conn.recv(1024))
    print('Content = %s' % request)
    enable = request.find('/?enable')
    start_rec = request.find('/?start_rec')
    
    print('STATE is: '+state)
    
    if start_rec == 6:
        writing = 1
        print ('Data recording enabled')
    if enable == 6:
        print('Enabling movement')
        state = 'ENABLED'
        writing = robot_movement(writing,state)
        print('robot_movement returned: ' + str(writing))
        state = 'DISABLED'
    print('State sent to web page is: ' + state)
    response = web_page(state)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
