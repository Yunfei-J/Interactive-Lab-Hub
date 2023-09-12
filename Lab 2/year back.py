import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
import tkinter as tk


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image0 = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image0)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image0, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


current_year = 2023
year_bk_1 = 1983
# 1983,1969,1939,1903
year_bk_2 = 1973 
year_bk_3 = 1943
year_bk_3 = 1903

image = Image.open("red.jpg")
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


# Scale the image to the smaller screen dimension
image_ratio = image.width / image.height
screen_ratio = width / height
if screen_ratio < image_ratio:
    scaled_width = image.width * height // image.height
    scaled_height = height
else:
    scaled_width = width
    scaled_height = image.height * width // image.width
image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

# Crop and center the image
a = scaled_width // 2 - width // 2
b = scaled_height // 2 - height // 2
image = image.crop((a, b, a + width, b + height))



initial_time = int(time.time()) #frame of reference in seconds

def delta_sleep(s):
    """
    Parameters:
        s: seconds since elapsed to sleep until
    """
    if int(time.time()) > initial_time + s:
        # check if the delta time has already passed
        return
    else:
        # find time needed to sleep to reach the specified param 's'
        needed_sleep = (initial_time+s) - int(time.time())
        time.sleep(needed_sleep)


while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=400)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    y = top
    display_time = strftime("%m/%d/%Y %H:%M:%S")
    # draw.text((x, y), display_time, font=font, fill="#FFFFFF")
    
    if current_year > 1983:
        draw.text((x, y), str(current_year), font=font, fill="#FFFFFF")
        print(current_year)
        disp.image(image0, rotation)
        current_year -= 10
    elif current_year == 1983:
        disp.image(image,rotation)
        delta_sleep(5)
        disp.image(image0, rotation)
        draw.text((x, y),'<<1983>>', font=font, fill="#FFFFFF")
        current_year -= 5
    elif current_year > 1973 and current_year <1983:
        draw.text((x, y), str(current_year), font=font, fill="#FFFFFF")
        print(current_year)
        disp.image(image0, rotation)
        current_year -= 5
    elif current_year == 1973: 
        disp.image(image,rotation)
        delta_sleep(5)
        # current_year -= 10
        # disp.image(image0, rotation)
        # draw.text((x, y),str(current_year), font=font, fill="#FFFFFF")
    
    

    

    # Display image.
    disp.image(image0, rotation)
    time.sleep(0.05)
