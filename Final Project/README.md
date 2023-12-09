# Project plan: Big idea, timeline, parts needed, fall-back plan.
## Big Idea: The user can set timers,by physical knobs,to control multiple stoves to turn on, turn off, or adjust power

## Specific Application: A control panel comprising four rotary encoders or joysticks and some LED signal lights is used to set time for individual stove’s action such as turning on, off, or changing power level. To physically rotate the stove knobs, we want to provide the option of remotely controlling a servo motor to do the job for the user.

Well Done is a stove add-on system that offers an individual timer for each stove to save users from the trouble of keeping track of the cooking time themselves.

## Timeline: 
Nov 14: Set proposal
Nov 21: Scout for suitable rotary encoders, buttons,  joystick, and LED signal lights. Envision its final appearance on actual stove
Nov 28 & 30: Code timer-setting program and alert-sending system with MQTT
Dec 5 & 7: Design and produce costumes for “Well Done”. 
Dec 14: User-testing and finish write-up

## Expected Challenges:
May not find four rotary encoders
Servo motor may not be powerful enough to turn the knob and if it could do precise turns
Fall-back plan: 
use joysticks as substitute for rotary encoders
Discard the remote knob-turning feature

## Contribution Overview:
Together: Scout resources, design costumes
Jamie: Develop timer-setting program and alert-sending system
Fei: Develop LED feedback program and produce costume

# Documentation of design process
## Ideation
Storyboard
Richard is cooking. He is cooking two pots of food at the same time.

He needs to set separate timers to time the duration of cooking. Setting up different timers for different pots is troublesome for Richard.


He learned about WellDone, a stovetop add-on that can help him time different stove’s cooking time independently.


When the stove is complete cooking, Richard receives a text message informing him that stove No.X is done cooking!


## Execution
Program
Drafted the preliminary design plan: use rotary encoders to register the cooking time that the user wants to assign each of the stoves with. Once the time is up for a stove, a text message will be sent to the user’s phone.
Implemented individually working count-down timers
Applied multi-threading to enable timers working concurrently
Tried display with ST7735 screen but ended up paralyzing both Raspberry Pis we owned.
Replaced with a new Pi
Wrote script to show real-time positions of the rotary encoders, start counting down once the encoder knob is pressed, and display “Done” when the time left hits zero. 
Improved message readability by adjust their alignment and color 

## Device costume
Drafted a rough layout of the stovetop in Adobe Illustrator

Measured the dimensions of needed components (e.g. Pi, Pi screen, rotary encoder platform, etc.)
Changed from horizontal to portrait layout design

Laser cut steps:
Cut out the box structure
Vector cut holes for screen, fake cooking power knobs, and rotary encoders
Vector cut “add-ons”: stoves, knobs 
Raster cut our Logo and names
Embellished the box surface with reflective silver material

## Hardware
Soldered the back of Adafruit rotary encoders to modify each’s i2C address
Connected all parts to MiniPi TFT screen with jumpers as following:


# Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)

# Video of someone using your project
https://drive.google.com/file/d/1V_nF6uEfMx32FJ5AoiEJPgi34Yzn_owL/view?usp=sharing

# Reflections on process (What have you learned or wish you knew at the start?)
More research and thorough initial planning: 
Screen for display
Eyespi couldn’t function
Mini OLED doesn’t light up
Testing for screens wasted time for laser cut planning

Conducting screen tests before laser cut planning proved to be a time-consuming detour. Future projects should prioritize comprehensive planning to ensure a more efficient and purposeful prototyping process. Encountering difficulties with the Mini OLED not lighting up highlighted the necessity of thorough pre-research on component compatibility. A deeper understanding of each component's specifications during the planning phase could prevent unforeseen issues during the prototyping process. 

Battery case needed for PI to run
Specific power banks that PI can run on

A battery case was necessary for the Raspberry Pi's functionality. It shows us the importance of early consideration of power requirements. Identifying specific power banks compatible with the Raspberry Pi in the early stages would optimize testing efforts and resource allocation.

3D printing of knobs
Failed because model can’t be glued to printer surface
Laser cut
Originally used a thicker board, and the rotary encoder couldn’t be fixed to the board
With Pi’s raised interface (ports), it is difficult to have only the screen popping out and the rest of the interface hidden

Challenges in 3D printing and fixing the rotary encoder to the board emphasized the critical role of material selection and manufacturing techniques. Early experimentation with materials and prototyping methods could mitigate complications in later stages.The unique architecture of the Raspberry Pi, particularly its raised interface (ports), posed unexpected design challenges. Awareness of device architecture at the project's outset would enable more thoughtful and innovative design solutions, avoiding complexities during implementation.

# Group work distribution questionnaire
Jamie
Timer logic programming
Laser Cut
Device Design
Hardware assembly
Yunfei
Timer logic programming
Laser Cut
Device Design
Hardware assembly
