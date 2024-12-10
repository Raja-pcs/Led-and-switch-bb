import Adafruit_BBIO.GPIO as GPIO
import time

# Setup GPIO pins
LED_PIN = "P9_12"  # GPIO1_28 (Change this as per your connection)
SWITCH_PIN = "P9_41"  # GPIO1_16 (Change this as per your connection)

# Set up GPIO mode and pins
GPIO.setup(LED_PIN, GPIO.OUT)  # Set LED pin as output
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set switch pin as input with pull-up resistor

# Main loop
try:
    while True:
        # Read the switch state
        switch_state = GPIO.input(SWITCH_PIN)
        
        if switch_state == GPIO.LOW:  # Button pressed (active low)
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
        else:
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED

        time.sleep(0.1)  # Debounce delay

except KeyboardInterrupt:
    print("Exiting program.")
    GPIO.cleanup()  # Clean up GPIO on exit
