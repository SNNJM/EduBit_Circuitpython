import time
import rtc
import board
import busio
import simpleio
import rotaryio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

buzzer = board.GP22
NOTE_C4 = 261
NOTE_G4 = 392
NOTE_F4 = 784

IR1 = board.GP3
IR2 = board.GP2
sensor = rotaryio.IncrementalEncoder(IR1, IR2)

LCD_SCL = board.GP5
LCD_SDA = board.GP4
LCD_ADDR = 0x27
i2c_lcd = busio.I2C(LCD_SCL, LCD_SDA)
lcd = LCD(I2CPCF8574Interface(i2c_lcd, LCD_ADDR), num_rows=2, num_cols=16)

r = rtc.RTC()
r.datetime = time.struct_time((2023, 8, 1, 0, 0, 0, 0, -1, -1))

day = str(r.datetime.tm_mday)
lcd.print(day)
lcd.print("/")
month = str(r.datetime.tm_mon)
lcd.print(month)
lcd.print("/")
year = str(r.datetime.tm_year)
lcd.print(year)
lcd.print("\n")

hour = str(r.datetime.tm_hour)
lcd.print(hour)
lcd.print("-")
minit = str(r.datetime.tm_min)
lcd.print(minit)
lcd.print("-")
sec = str(r.datetime.tm_sec)
lcd.print(sec)




#time.sleep(5)
#lcd.print("Bidirectional\nVisitor Counter")
simpleio.tone(buzzer, NOTE_C4, duration=0.1)
simpleio.tone(buzzer, NOTE_G4, duration=0.15)
time.sleep(1)

lcd.clear()
lcd.print("No of visitor:\n0")


last_count = 0

def button(num):
        if num==1:
            lcd.set_cursor_pos(1, 0)
            month = str(r.datetime.tm_mon)
            lcd.print("Bulan:")
            lcd.print(month)
            

        elif num==2:
            lcd.set_cursor_pos(1, 0)
            day = str(r.datetime.tm_mday)
            lcd.print(day)
            lcd.print("/")
            month = str(r.datetime.tm_mon)
            lcd.print(month)
            lcd.print("/")
            year = str(r.datetime.tm_year)
            lcd.print(year)

        elif num==3:
            lcd.set_cursor_pos(1, 0)
            lcd.print("Clear")
            count=0
            
last_count = 0
while True:

    button(2)

    day = str(r.datetime.tm_mday)

    month = str(r.datetime.tm_mon)

    year = str(r.datetime.tm_year)


    hour = str(r.datetime.tm_hour)

    minit = str(r.datetime.tm_min)

    sec = str(r.datetime.tm_sec)
    lcd.set_cursor_pos(1, 14)
    lcd.print(sec)
##    if sec=="15":
##        simpleio.tone(buzzer, NOTE_G4, duration=0.5)
##        count = 0
 

    count = sensor.position
    
        if count != last_count:
            print("Visitor:{}".format(count))
            lcd.set_cursor_pos(0, 14)
            lcd.print("{} ".format(count))
            
            if count > last_count:
                simpleio.tone(buzzer, NOTE_G4, duration=0.1)
            else:
                simpleio.tone(buzzer, NOTE_C4, duration=0.1)
                
        
            last_count = count

    
##        today = str(r.datetime.tm_mday)
##        if day>today:
##            last_count = count
##        else:
##            last_count = 0
##            lcd.print(today)



