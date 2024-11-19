import Adafruit_BBIO.GPIO as GPIO
import time

# Pin Definitions for LEDs
LED1 = "P9_14"
LED2 = "P9_16"
LED3 = "P9_18"
LED4 = "P9_22"

# Pin Definitions for Switches
SWITCH1 = "P9_11"
SWITCH2 = "P9_13"
SWITCH3 = "P9_15"
SWITCH4 = "P9_17"

# Set up GPIO for LEDs
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

# Set up GPIO for Switches (input with pull-down resistors)
GPIO.setup(SWITCH1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Function to check switches and control LEDs
def control_leds():
    # Read switch states
    switch1_state = GPIO.input(SWITCH1)
    switch2_state = GPIO.input(SWITCH2)
    switch3_state = GPIO.input(SWITCH3)
    switch4_state = GPIO.input(SWITCH4)
    
    # Control LED1 based on SWITCH1
    if switch1_state == GPIO.HIGH:
        GPIO.output(LED1, GPIO.HIGH)  # Turn on LED1
    else:
        GPIO.output(LED1, GPIO.LOW)   # Turn off LED1
    
    # Control LED2 based on SWITCH2
    if switch2_state == GPIO.HIGH:
        GPIO.output(LED2, GPIO.HIGH)  # Turn on LED2
    else:
        GPIO.output(LED2, GPIO.LOW)   # Turn off LED2
    
    # Control LED3 based on SWITCH3
    if switch3_state == GPIO.HIGH:
        GPIO.output(LED3, GPIO.HIGH)  # Turn on LED3
    else:
        GPIO.output(LED3, GPIO.LOW)   # Turn off LED3
    
    # Control LED4 based on SWITCH4
    if switch4_state == GPIO.HIGH:
        GPIO.output(LED4, GPIO.HIGH)  # Turn on LED4
    else:
        GPIO.output(LED4, GPIO.LOW)   # Turn off LED4

try:
    while True:
        control_leds()  # Continuously check switches and update LEDs
        time.sleep(0.1)  # Small delay to avoid excessive CPU usage

except KeyboardInterrupt:
    print("Program terminated")

finally:
    GPIO.cleanup()
