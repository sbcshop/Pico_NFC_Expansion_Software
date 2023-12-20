from machine import Pin, I2C
from nfc import oled

i2c = I2C(0,scl=Pin(21), sda=Pin(20), freq=100000)
print(i2c)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))   
display = oled(128, 32, i2c)

display.text('Hello World', 0, 20, 2)
display.show()