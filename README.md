# rover_diy
Personal project used to teach myself programming using Python (micropython) for the ESP32 microncontroller, HTML and a bit of CSS and Javascript for the web interface,
and, later, Java/Kotlin for creating an Android app able to control the rover both via WiFi and via Bluetooth.

The rover platform is 3D printed in PLA on my Anycubic Mega Zero printer and can be found here (https://www.thingiverse.com/thing:3112734) - I am not the designer 
of the platform.

The rover is currently controlled via WiFi using the ESP32 microcontroller.

The tracks are powered by 2 TT geared DC motors as seen here: https://www.ebay.co.uk/itm/193732734105?var=493956859038

The DC motors are controlled via an DRV8833 controller and powered from a generic USB power bank. The power bank has 2 ports each capable of up to 2A and allows the
microcontroller and motors to be powered separately.

THe rover will eventually include a 3D printed robotic arm as seen here https://www.thingiverse.com/thing:34829 (not my design), powered by 5 9G micro servos controlled
via a PCA9685 servo controller.

The plan is to add a microSD module to allow large logs to be recorded and stored on-board as well as the following sensors:
- MPU-6050 Gyro-accelerometer
- GY-NEO6MV2 GPS Module
- Ultrasonic range sensor

These sensors will allow a certain level of autonomy and allow me to learn and apply more programming concepts.

