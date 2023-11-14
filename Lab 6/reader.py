import paho.mqtt.client as mqtt
import uuid
import ssl

import board
import busio
import adafruit_apds9960.apds9960
import time
import paho.mqtt.client as mqtt
import uuid
import signal
import ssl

import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

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

height =  disp.height
width = disp.width 
image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)


i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_color = True
r, g, b, a = sensor.color_data

topic = 'IDD/colors'


#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
	print(f"connected with result code {rc}")
	client.subscribe(topic)

    draw.rectangle((0, height*0.5, width, height), fill=color[:3])
    disp.image(image)
    time.sleep(.01)
	# you can subsribe to as many topics as you'd like
	# client.subscribe('some/other/topic')

def on_message(client, userdata, msg):
    print(f"topic: {msg.topic} msg: {msg.payload.decode('UTF-8')}")
    # if a message is recieved on the colors topic, parse it and set the color
    if msg.topic == topic:
        colors = list(map(int, msg.payload.decode('UTF-8').split(',')))
        draw.rectangle((0, 0, width, height*0.5), fill=color)
        disp.image(image)


client = mqtt.Client(str(uuid.uuid1()))
client.tls_set(cert_reqs=ssl.CERT_NONE)
client.username_pw_set('idd', 'device@theFarm')
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

client.loop_start()

# this lets us exit gracefully (close the connection to the broker)
def handler(signum, frame):
    print('exit gracefully')
    client.loop_stop()
    exit (0)

# hen sigint happens, do the handler callback function
signal.signal(signal.SIGINT, handler)



# the # wildcard means we subscribe to all subtopics of IDD
topic = 'IDD/#'


# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set(cert_reqs=ssl.CERT_NONE)
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

# this is blocking. to see other ways of dealing with the loop
#  https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
client.loop_forever()



# our main loop
# while True:
    # r, g, b, a = sensor.color_data
	

    # color =tuple(map(lambda x: int(255*(1-(a/65536))*255*(x/65536)) , [r,g,b,a]))

    # # if we press the button, send msg to cahnge everyones color
    # if not buttonA.value:
    #     client.publish(topic, f"{r},{g},{b}")
    # draw.rectangle((0, height*0.5, width, height), fill=color[:3])
    # disp.image(image)
    # time.sleep(.01)
    
