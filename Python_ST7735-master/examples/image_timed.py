# # Copyright (c) 2014 Adafruit Industries
# # Author: Tony DiCola
# #
# # Permission is hereby granted, free of charge, to any person obtaining a copy
# # of this software and associated documentation files (the "Software"), to deal
# # in the Software without restriction, including without limitation the rights
# # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# # copies of the Software, and to permit persons to whom the Software is
# # furnished to do so, subject to the following conditions:
# #
# # The above copyright notice and this permission notice shall be included in
# # all copies or substantial portions of the Software.
# #
# # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# # THE SOFTWARE.
# from PIL import Image
# import time

# # import st7735 as TFT
# import Adafruit_GPIO as GPIO

# # import Adafruit_GPIO.SPI as SPI


# WIDTH = 128
# HEIGHT = 160
# SPEED_HZ = 4000000


# # # Raspberry Pi configuration.
# # DC = 24
# # RST = 25
# # SPI_PORT = 0
# # SPI_DEVICE = 0

# # BeagleBone Black configuration.
# # DC = 'P9_15'
# # RST = 'P9_12'
# # SPI_PORT = 1
# # SPI_DEVICE = 0

# # # Create TFT LCD display class.
# # disp = TFT.ST7735(
# #     DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=SPEED_HZ)
# # )

# import board
# import digitalio
# import adafruit_rgb_display.st7735 as TFT

# # ...

# spi = board.SPI()
# tft_cs = digitalio.DigitalInOut(board.CE0)
# tft_dc = digitalio.DigitalInOut(board.D25)
# tft_res = None

# disp = TFT.ST7735(spi, cs=tft_cs, dc=tft_dc, rst=tft_res, width=1600, height=800)


# # Initialize display.
# # disp.begin()


# print("Press Ctrl-C to exit")
# while True:
#     # Draw the image on the display hardware.
#     print("Drawing image")
#     start_time = time.time()

#     # Load an image
#     image = Image.open("cat.jpg")
#     # Resize the image and rotate it so matches the display.
#     image = image.rotate(90).resize((WIDTH, HEIGHT))

#     # Display the image on the screen
#     disp.image(image)
#     # disp.display(image)

#     end_time = time.time()
#     print("Time to draw image: " + str(end_time - start_time))
#     # disp.clear((0, 0, 0))

#     # Clear the display by filling it with a specified color (e.g., black)
#     disp.fill(0)  # 0 represents black in RGB
#     # disp.image()
#     disp.image(image)


from PIL import Image, ImageDraw
import time
import board
import digitalio
import adafruit_rgb_display.st7735 as TFT

WIDTH = 160
HEIGHT = 80

spi = board.SPI()
tft_cs = digitalio.DigitalInOut(board.CE0)
tft_dc = digitalio.DigitalInOut(board.D25)
tft_res = digitalio.DigitalInOut(board.D24)  # Connect the reset pin to GPIO 24

disp = TFT.ST7735(spi, cs=tft_cs, dc=tft_dc, rst=tft_res, width=WIDTH, height=HEIGHT)

try:
    print("Press Ctrl-C to exit")
    while True:
        # Create a blank image
        image = Image.new("RGB", (WIDTH, HEIGHT), color=(0, 0, 0))
        draw = ImageDraw.Draw(image)

        # Draw a red square in the center
        square_size = 20
        draw.rectangle(
            (
                WIDTH // 2 - square_size // 2,
                HEIGHT // 2 - square_size // 2,
                WIDTH // 2 + square_size // 2,
                HEIGHT // 2 + square_size // 2,
            ),
            fill=(255, 0, 0),
        )

        # Display the image on the screen
        disp.image(image)

        # Pause for a moment (optional)
        time.sleep(2)

        # Clear the display by filling it with a specified color (e.g., black)
        disp.fill(0)

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    # Reset the display
    disp.reset()
