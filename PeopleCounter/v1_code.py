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

IR1 = board.GP3
IR2 = board.GP2
sensor = rotaryio.IncrementalEncoder(IR1, IR2)

LCD_SCL = board.GP5
LCD_SDA = board.GP4
LCD_ADDR = 0x27
i2c_lcd = busio.I2C(LCD_SCL, LCD_SDA)
lcd = LCD(I2CPCF8574Interface(i2c_lcd, LCD_ADDR), num_rows=2, num_cols=16)

r = rtc.RTC()
#r.datetime = time.struct_time((2023, 8, 7, 10, 33, 10, 0, -1, -1))

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

while True:

    count = sensor.position
    
    if count != last_count:
        print("No of visitor: {} ".format(count))
        lcd.set_cursor_pos(1, 0)
        lcd.print("{} ".format(count))
        
        if count > last_count:
            simpleio.tone(buzzer, NOTE_G4, duration=0.1)
        else:
            simpleio.tone(buzzer, NOTE_C4, duration=0.1)
        
        last_count = count
