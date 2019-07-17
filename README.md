# Python I2CLCD module

Python I2CLCD module for LCD1602/2002/2004 screen with I2C adapter  
Can be used on embedded devices like the Raspberry Pi

## Features

- Implemented most of the built-in instructions of LCD1602/2002/2004
- Support for custom characters
- Support backlight settings
- Support 'Cursor or Display Shift' instructions
- Hints for each method

## Quick start

```python
import i2clcd

lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x27, lcd_width=16)
lcd.init()

# fill a line by the text
lcd.print_line('hello', line=0)
lcd.print_line('world!', line=1, align='RIGHT')

# print text at the current cursor position
lcd.move_cursor(1, 0)
lcd.print('the')

# custom character
char_celsius = (0x10, 0x06, 0x09, 0x08, 0x08, 0x09, 0x06, 0x00)
lcd.write_CGRAM(char_celsius, 0)
lcd.move_cursor(0, 6)
lcd.print(b'CGRAM: ' + i2clcd.CGRAM_CHR[0])
```
![A photo for the result](https://i.loli.net/2019/07/17/5d2e027e2cbb890498.jpg)
