import machine
import time
import binascii
import array
import ustruct
import urandom
from micropython import const
import framebuf

STARTBYTE     ='A8'  
ENDBYTE       ='A9'
HARD_VERSION  ='0007000100'
GET_ADDRESS   ='0001000100'
READ_DATA     ='0037000200'         
NTAG_VERSION  ='0036000100'
ECC_SIG       ='003C000100'
WRITE_DATA    ='0039000600'
CARD_UID      ='0026000100' 

# register definitions
SET_CONTRAST = const(0x81)
SET_ENTIRE_ON = const(0xA4)
SET_NORM_INV = const(0xA6)
SET_DISP = const(0xAE)
SET_MEM_ADDR = const(0x20)
SET_COL_ADDR = const(0x21)
SET_PAGE_ADDR = const(0x22)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP = const(0xA0)
SET_MUX_RATIO = const(0xA8)
SET_COM_OUT_DIR = const(0xC0)
SET_DISP_OFFSET = const(0xD3)
SET_COM_PIN_CFG = const(0xDA)
SET_DISP_CLK_DIV = const(0xD5)
SET_PRECHARGE = const(0xD9)
SET_VCOM_DESEL = const(0xDB)
SET_CHARGE_PUMP = const(0x8D)

class NFC():
    def __init__(self,baudrate):
        self.serial = machine.UART(0, baudrate=baudrate, bits=8, parity=None, stop=1, tx=machine.Pin(0), rx=machine.Pin(1))
        self.serial.init(baudrate=baudrate, bits=8, parity=None, stop=1)
        time.sleep(0.2)

    def calculate_checksum(self,data):
        checksum = 0
        for byte in data:
            checksum ^= byte
        return checksum

    def calculation(self,address_r):
        address_r = str(hex(int(address_r))[2:])
        if len(address_r) < 2:
            address_r = '0' + address_r            
        rand_hex = self.random_hex()
        chksm_data = rand_hex+READ_DATA+address_r
        bin_data1 = binascii.unhexlify(chksm_data)
        chk_1 = (hex(self.calculate_checksum(bin_data1)))
        chk = chk_1[2:]
        dat = STARTBYTE+rand_hex+READ_DATA+address_r+chk+ENDBYTE
        return dat
    
    def calculation_1(self,da):           
        rand_hex_1  = self.random_hex()
        chksm_data_1  = rand_hex_1 +da
        bin_data1_1  = binascii.unhexlify(chksm_data_1 )
        chk_2 = (hex(self.calculate_checksum(bin_data1_1 )))
        chk_1  = chk_2[2:]
        dat_1  = STARTBYTE+rand_hex_1 +da+chk_1 +ENDBYTE
        return dat_1 

    def write_calculation(self,data,address_r,s):
        address_r = str(hex(int(address_r))[2:])
        if len(address_r) < 2:
            address_r = '0' + address_r            
        rand_hex = self.random_hex()
        chksm_data = rand_hex+s+address_r+data
        bin_data1 = binascii.unhexlify(chksm_data)
        chk_1 = (hex(self.calculate_checksum(bin_data1)))
        chk = chk_1[2:]
        dat = STARTBYTE+rand_hex+s+address_r+data+chk+ENDBYTE
        return dat
    
        
    def random_hex(self):
        length = 2
        random_bytes = bytearray(urandom.getrandbits(8) for _ in range((length + 1) // 2))
        random_hex = ''.join('{:02x}'.format(byte) for byte in random_bytes)
        return random_hex[:length]
           
    def send_command(self, Data):
        bin_data = binascii.unhexlify(Data)
        response = self.serial.write(bin_data)
        #print("bin_data = ",bin_data)

    def hardware_version(self):
        dat_1  = self.calculation_1(HARD_VERSION)
        self.send_command(dat_1 )
        time.sleep(0.2)
        d = self.serial.read(19)
        s = []
        if d is not  None: 
            def split_bytes_data(data, packet_size):
                # Split the bytes object into packets of the specified size
                packets = [data[i:i+packet_size] for i in range(0, len(data), packet_size)]
                return packets
            ds = split_bytes_data(d,7)
            for i in range(1,len(ds)):
                   s.append(str(ds[i],'latin-1'))
            return "".join(s)

########################## read operations ############################################
    def data_read(self,address_r):
        dat = self.calculation(address_r)
        if len(dat) == 20:
            data = self.send_command(dat)
            time.sleep(0.2)
            rec_data = self.serial.read()
            if rec_data is not None:
                a = ['{:02x}'.format(x) for x in rec_data]
                if "".join(a)[6:14] != "37000101":
                    if  len("".join(a)[14:22]) > 7:
                        return "".join(a)[14:22]
                    else:
                        return "Card not detect"
        
    def Ntag_version(self):
        dat = self.calculation_1(NTAG_VERSION)
        data = self.send_command(dat)
        time.sleep(0.5)
        rec_data = self.serial.read()
        #print("rec_data = ",rec_data)
        if rec_data is not None:
            a = ['{:02x}'.format(x) for x in rec_data]
            return "".join(a)
        #read_data.flush()
        
    def ECC_signature(self):
        dat = self.calculation_1(ECC_SIG)
        if len(dat) == 18:
            data = self.send_command(dat)
            time.sleep(0.5)
            rec_data = self.serial.read()
            #print("rec_data = ",rec_data)
            if rec_data is not None:
                a = ['{:02x}'.format(x) for x in rec_data]
                f =  "".join(a)[-5:-4]
                
                if  "".join(a)[-5:-4] == '1':
                    return "Card not detect"
                else:
                    return  "".join(a)
        
    def Card_UID(self):
        dat = self.calculation_1(CARD_UID)
        print(dat)
        print(len(dat))
        if len(dat) == 18:
            data = self.send_command(dat)
            time.sleep(0.5)
            rec_data = self.serial.read()
            if rec_data is not None and len(rec_data) > 18:
                a = ['{:02x}'.format(x) for x in rec_data]
                s = "".join(a)
                return s#s[-36:-1]
        
########################## write operations ############################################
        
    def Data_write(self,data,address_r):
        dat = self.write_calculation(data,address_r,WRITE_DATA)
        if len(dat) == 28:
            data = self.send_command(dat)
            time.sleep(0.5)
            rec_data = self.serial.read()
            if rec_data is not None:
                a = ['{:02x}'.format(x) for x in rec_data]
                f =  "".join(a)[-5:-4]
                
                if  "".join(a)[-5:-4] == '0':
                    return "Card write sucessfully"
                else:
                    return "Card not detect"
        

# Subclassing FrameBuffer provides support for graphics primitives
# http://docs.micropython.org/en/latest/pyboard/library/framebuf.html
class SSD1306(framebuf.FrameBuffer):
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def init_display(self):
        for cmd in (
            SET_DISP | 0x00,  # off
            # address setting
            SET_MEM_ADDR,
            0x00,  # horizontal
            # resolution and layout
            SET_DISP_START_LINE | 0x00,
            SET_SEG_REMAP | 0x01,  # column addr 127 mapped to SEG0
            SET_MUX_RATIO,
            self.height - 1,
            SET_COM_OUT_DIR | 0x08,  # scan from COM[N] to COM0
            SET_DISP_OFFSET,
            0x00,
            SET_COM_PIN_CFG,
            0x02 if self.width > 2 * self.height else 0x12,
            # timing and driving scheme
            SET_DISP_CLK_DIV,
            0x80,
            SET_PRECHARGE,
            0x22 if self.external_vcc else 0xF1,
            SET_VCOM_DESEL,
            0x30,  # 0.83*Vcc
            # display
            SET_CONTRAST,
            0xFF,  # maximum
            SET_ENTIRE_ON,  # output follows RAM contents
            SET_NORM_INV,  # not inverted
            # charge pump
            SET_CHARGE_PUMP,
            0x10 if self.external_vcc else 0x14,
            SET_DISP | 0x01,
        ):  # on
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        self.write_cmd(SET_DISP | 0x00)

    def poweron(self):
        self.write_cmd(SET_DISP | 0x01)

    def contrast(self, contrast):
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def show(self):
        x0 = 0
        x1 = self.width - 1
        if self.width == 64:
            # displays with width of 64 pixels are shifted by 32
            x0 += 32
            x1 += 32
        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(x0)
        self.write_cmd(x1)
        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        self.write_data(self.buffer)


class oled(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        self.write_list = [b"\x40", None]  # Co=0, D/C#=1
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.temp[0] = 0x80  # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        self.write_list[1] = buf
        self.i2c.writevto(self.addr, self.write_list)

