# Pico_NFC_Expansion_Software

<img src="https://github.com/sbcshop/Pico_NFC_Expansion_Software/blob/main/images/img1.png">

Pico NFC Expansion 13.56 MHz frequency-based NFC Reader/Writer. 
This Github provides a getting started guide and other working details for the NFC Expansion.

### Features:
- Onboard 13.56MHz NFC read/write Module
- 0.91 inch OLED
- Drag- and- drop programming using mass storage over USB
- Type C Power/UART
- Multifunction GPIO breakout supporting general I/O, UART, I2C, SPI, ADC & PWM function.
- Multi-tune Buzzer to add audio alert into the project
- Status LED for board power, and Tag Scan indication 
- Multi-platform support like MicroPython, CircuitPython, and Arduino IDE.
- Comes with HID support, so the device can simulate a mouse or keyboard 

### Specifications:
- Operating voltage of pins 3.3V and board supply 5V
- Operating Frequency: 13.56MHz
- Operating current: 50mA
- Reading Distance: >50mm(The effective distance is related to the IC card and the use environment)
- Integrated Antenna
- Support Protocols: ISO14443A, ISO14443B, Sony, ISO15693, ISO18092
- Contactless cards: NTAG213, Mifare one S50, Mifare one S70, ultralight, FM11RF08
- Operating Temperature: -15°C~+55°C

## Getting Started with NFC Expansion
### Hardware Overview
#### Pinout
<img src="https://github.com/sbcshop/Pico_NFC_Expansion_Software/blob/main/images/img.png">

### Interfacing Details
- Pico W/Pico and RFID module interfacing
  
  | Pico W | NFC Module Pin | Function |
  |---|---|---|
  |GP1 | RX | Serial UART connection |
  |GP0 | TX  | Serial UART connection |


- Buzzer and OLED Interfacing
  
  | Pico W | Buttons | Function |
  |---|---|---|
  |GP20 | SDA |OLED Pin|
  |GP21 | SCL |OLED Pin|
  |GP2  | Buzzer | Buzzer positive |
 
- Breakout Pins of NFC
  | Pico W | Function |
  |---|---|
  |BEEP | NFC buzzer Pin |
  |NFC_RX | NFC Pin |
  |NFC_TX | NFC Pin |
  |GND    | NFC Pins|
  |VCC    | NFC Pins|

### 1. Step to install boot Firmware in Pico
   - Push and hold the BOOTSEL button and plug your Pico W into the USB port of your computer. Release the BOOTSEL button after your Pico is connected.
   <img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/pico_bootmode.gif">
   
   - It will mount as a Mass Storage Device called RPI-RP2.
   - Drag and drop the MicroPython UF2 - [ReadPi_firmware](https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/ReadPi_Firmware.uf2) file provided in this github onto the RPI-RP2 volume. Your Pico will reboot. You are now running MicroPython on ArdiPi.

### 2. Onboard LED Blink 
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Once done start **Thonny IDE application**, Connect Expansion to laptop/PC.
   - Select the device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
     
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img1.jpg" />
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img2.jpg" />
      
   - Write simple onboard blink Python code or [Download Led blink code](https://github.com/sbcshop/Pico_NFC_Expansion_Software/blob/main/examples/pico_onboard_ledBlink.py), then click on the green run button to make your script run on Pico.
     
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img3.jpg" />
     
     Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug Pico, it will stop running. To run your script without using an IDE, simply power up ArdiPi and it should run your script, go to step 3. Once you have transferred your code to the ArdiPi board, to see your script running, just plug in power either way using micro USB or via Vin, both will work.

### 3. How to move your script on Pico W of Expansion
   - Click on File -> Save Copy -> select Raspberry Pi Pico , Then save file as main.py
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/transfer_script_pico.gif" />
   
      Similarly, you can add various Python code files to Pico. Also, you can try out sample codes given here in [examples folder](https://github.com/sbcshop/Pico_NFC_Expansion_Software/tree/main/examples). 
   
   - But in case you want to move multiple files at one go, for example, suppose you are interested in saving the library files folder into Pico W, the below image demonstrates that
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/images/multiple_file_transfer.gif" />
   
**NOTE: Don't rename _lib_ files** or other files, only your main code script should be renamed as main.py for standalone execution without Thonny.


### Example Codes
   Save whatever example code file you want to try as **main.py** in **Pico W** as shown above [step 3](https://github.com/sbcshop/ReadPi_NFC_Software/tree/main#3-how-to-move-your-script-on-pico-w-of-readpi), also add related lib files with the default name.
   In [example](https://github.com/sbcshop/Pico_NFC_Expansion_Software/tree/main/examples) folder you will find demo example script code to test onboard components of Expansion like 
   - [NFC module demo](https://github.com/sbcshop/Pico_NFC_Expansion_Software/blob/main/examples/main.py): testing onboard NFC module, buzzer and display unit of the shield. For this demo code to test you will have to add lib [nfc. py](https://github.com/sbcshop/Pico_NFC_Expansion_Software/blob/main/examples/nfc.py)

### Working Without Pico (Via USB)
   Find more details in [NTAG Datasheet]( https://github.com/sbcshop/NFC_Module)
   
  #### Working Description with NFC module:
   
  - Basic Communication Protocol: Data Format

    <img src="https://github.com/sbcshop/ReadPi_NFC_Software/blob/main/images/NFC_Communication_protocol.png">
   
  - Description of bytes in the data packet: 

     | Field | Length| Description | Remark |
     |---|---|---|---|
     |STX | 1  | 0xa8 - ‘Start Byte’ – Standard control bytes. Indicates the start of a data packet  | |
     |SEQ1 | 1  | Random Code  | Address bits are reserved for handling device addresses over 255.|
     |DADD | 1  | Device address is used for multiple machine communication, only address matching can be used for data communication, 0x00 and 0xFF addresses are broadcast addresses  |  |
     |CMD | 1  | Command Code One byte of the command sent by the upper unit to the lower unit  | |
     |DATA LENGTH | 2  | Data length includes TIME/STATUS + DATA field  | The high byte comes first, the low byte comes second |
     |STATUS | 1  | Lower computer return status, one byte | 00 means the command is executed correctly and the others are error codes |
     |TIME | 1  | Used for specific command time control, timeout processing, and other commands (most) the parameter is 0  | |
     |DATA  [0-N] | 2000  | Command Code One byte of the command sent by the upper unit to the lower unit  | It is used as command parameters when sent by the upper computer and as return data when sent by the lower computer with variable length. The maximum length is 512, and it will not be processed when it is out of range. It will reply directly/show that the command is too long and wait for the next command. |
     |BCC | 1  | Xor check bit, which verifies data but does not contain STX and ETX |  |
     |ETX | 1  | 0xa9 - ‘Terminating byte’ – Standard control byte. Indicates the end of a data packet| |
    
    SYSTEM COMMANDS examples:

    CMD_GetAddress (0x01)
    ```
    Description: Get the device communication address
    Sending data：0x01
    Return Data：
    STATUS     0x00 - OK
    DATA[0]    Device Address

    ```
    CMD_SetBaudRate ( 0x03 )
    ```
    Description: Set the serial port baud rate
    Sending data：0x03
      DATA[0]
        0x00 – 9600 bps
        0x01 – 19200 bps
        0x02 – 38400 bps
        0x03 – 57600 bps
        0x04 – 76800 bps
        0x05 – 115200 bps
    Return Data：
        STATUS 0x00 - OK
    ```

   Checkout [Manual](https://github.com/sbcshop/Pico_NFC_Expansion_Software/blob/main/documents/NFC%20Module%20command%20Manual.pdf) for a detailed understanding of System and Working Commands to send module from Host and corresponding response getting from NFC Module. 

   #### Basic Memory Structure of NFC Tags 
   The EEPROM memory is organized into pages with 4 bytes per page. The NTAG213 variant has 45 pages, the NTAG215 variant has 135 pages and the NTAG216 variant has 231 pages in total. The functionality of the different memory sections is shown below for NTAG213. 

   <img src="https://github.com/sbcshop/Pico_NFC_Expansion_Software/blob/main/images/memory%20organization%20NTAG213.png">
   
  Find more details in [NTAG Datasheet](https://github.com/sbcshop/Pico_NFC_Expansion_Software/blob/main/documents/NTAG213_215_216.pdf)

   
## Resources
  * [Schematic](https://github.com/sbcshop/Pico_NFC_Expansion_Hardware/blob/main/Design%20Data/SCH.pdf)
  * [Hardware Files](https://github.com/sbcshop/Pico_NFC_Expansion_Hardware)
  * [Step File](https://github.com/sbcshop/Pico_NFC_Expansion_Hardware/blob/main/Mechanical%20Data/NFC%20EXPANSION.step)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)
  * [NFC Module Command Manual](https://github.com/sbcshop/Pico_NFC_Expansion_Software/blob/main/documents/NFC%20Module%20command%20Manual.pdf)
  * [NTAG213/215/216 Datasheet](https://github.com/sbcshop/Pico_NFC_Expansion_Software/blob/main/documents/NTAG213_215_216.pdf)


## Related Products
   * [Pinco NFC Expansion RFID](https://shop.sb-components.co.uk/products/readpi-an-rfid-nfc-reader-powered-with-raspberry-pi-pico-w?variant=40478483054675) - Pico NFC Expansion with 125KHz RFID powered by Raspberry Pi Pico W
   * [Raspberry Pi Pico RFID expansion](https://shop.sb-components.co.uk/products/raspberry-pi-pico-rfid-expansion) - RFID expansion board with support to incorporate Pico/Pico W 
   * [RFID_Breakout](https://shop.sb-components.co.uk/products/rfid-breakout?_pos=5&_sid=fac219786&_ss=r) - RFID breakout for standalone testing and freedom to choose microcontroller as per requirement.

## Product License

This is ***open source*** product. Kindly check the LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
