import Adafruit_BBIO.GPIO as GPIO
import time

# Define GPIO pins for the LEDs
leds = ["P9_12", "P9_14", "P9_16", "P9_18"]

# Setup the GPIO pins as output
for led in leds:
    GPIO.setup(led, GPIO.OUT)

# Blink the LEDs
try:
    while True:
        for led in leds:
            GPIO.output(led, GPIO.HIGH)  # Turn LED on
        time.sleep(0.5)  # Wait for half a second
        for led in leds:
            GPIO.output(led, GPIO.LOW)  # Turn LED off
        time.sleep(0.5)  # Wait for half a second

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on Ctrl+C exit
