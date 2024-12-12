import subprocess
import Adafruit_BBIO.GPIO as GPIO
import time

# GPIO setup
LED_PIN ="P9_12"  # Example GPIO pin for the LED
GPIO.setup(LED_PIN, GPIO.OUT)

def update_oled_display(message, x=1, y=2, rotate=False):
    """
    Update OLED display dynamically with optional rotation.

    Args:
        message (str): Text to display on OLED.
        x (int): X-coordinate of text.  
        y (int): Y-coordinate of text.
        rotate (bool): Whether to rotate/mirror the display.
    """
    # Base command
    command = f"./oled_bin -n 2 -x {x} -y {y} -l \"{message}\""

    # Add rotation flag if required
    if rotate:
        command += " --rotate"

    # Run the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("Output:", result.stdout)
    print("LED ON")
    print("Error:", result.stderr)
    print("LED OFF")

def control_led(state):
    """
    Control the LED and update the OLED display with its status.

    Args:
        state (bool): True to turn the LED on, False to turn it off.
    """
    if state:
        GPIO.output(LED_PIN, GPIO.HIGH)
        update_oled_display("LED: ON")
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        update_oled_display("LED: OFF")

# Example Usage
try:
    while True:
        # Turn LED on
        control_led(True)
        time.sleep(2)

        # Turn LED off
        control_led(False)
        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
