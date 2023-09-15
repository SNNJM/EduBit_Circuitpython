import time
import rtc
import board
import busio
import simpleio
import rotaryio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull



a=0

buzzer = board.GP22
NOTE_C4 = 261
NOTE_G4 = 392

IR1 = board.GP3
IR2 = board.GP2
sensor = rotaryio.IncrementalEncoder(IR1, IR2)
last_count = 0

LCD_SCL = board.GP5
LCD_SDA = board.GP4
LCD_ADDR = 0x27
i2c_lcd = busio.I2C(LCD_SCL, LCD_SDA)
lcd = LCD(I2CPCF8574Interface(i2c_lcd, LCD_ADDR), num_rows=2, num_cols=16)
lcd.set_backlight(1)


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

btn = DigitalInOut(board.GP8)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

prev_state = btn.value

while True:




    count = sensor.position
    lcd.set_cursor_pos(1, 0)
    lcd.print("{} ".format(a))
    
    if count != last_count:
        print("No of visitor: {} ".format(count))
        lcd.set_cursor_pos(1, 0)
        lcd.print("{} ".format(count))


        
        
        if count > last_count:
            simpleio.tone(buzzer, NOTE_G4, duration=0.1)
            a = a+1
            
        else:
            simpleio.tone(buzzer, NOTE_C4, duration=0.1)
        
        
        last_count = count
        
    cur_state = btn.value
    if cur_state != prev_state:
        if not cur_state:
            print("BTN is down")
            a=0
            
        else:
            print("BTN is up")
            
            

    prev_state = cur_state

