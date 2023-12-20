'''
Demo program to see how to read and write NFC tag
For the demo to run successfully you need to add lib file into Pico W :
'''
#import ssd1306
from machine import UART,Pin,SPI,PWM, I2C
import time,utime
from nfc import NFC
from nfc import oled
import os

buzzer = Pin(2, machine.Pin.OUT)
buzzer.value(0)

i2c = I2C(0,scl=Pin(21), sda=Pin(20), freq=100000)
print(i2c)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))   
display = oled(128, 32, i2c)

display.text("DEVICE START......", 0, 20, 2)
display.show()
time.sleep(2)
display.fill(0)
display.show()
            
data = '1B233A49' # must be 4 byte, for write
baudrate = 9600 # communication buadrate between pico W and NFC module
page_no = '15'    # memory location divided into pages NTAG213/215/216 -> 4bytes per page
nfc = NFC(baudrate) #create object
time.sleep(1) #wait for 1 second

while 1:
        status = nfc.Data_write(data,page_no) # Write data to Tag
        if status == "Card write sucessfully":
            dataRec = nfc.data_read(page_no) # Read Tag data written initially
            if dataRec is not None:
                print("Received data = ",dataRec)
                display.text(dataRec, 0, 10, 2)
                buzzer.value(1)
                display.show()
                time.sleep(0.2)
        else :
            print("Scan Card Please!")
            buzzer.value(0)
        
        time.sleep(0.5)
