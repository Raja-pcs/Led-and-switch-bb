#Connect to oled with beagle bone black C4 to C9 connectors 
import subprocess
def run_command(command):
    try:
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, check=True, stdout=subproc>
        print(f"Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error while running command: {e.stderr}")
# List of commands to run
commands = [
    "./oled_bin -n 2 -I 128x64",  # ①
    "./oled_bin -n 2 -I 128x32",  # ② (commented out in your original snippet)
    "./oled_bin -n 2 -c",         # ③
    "./oled_bin -n 2 -r 0",       # ④
    "./oled_bin -n 2 -x 1 -y 1",  # ⑤
    "./oled_bin -n 2 -l \"Hello World!!!!\""  # ⑥

]
# Run each command in sequence
for cmd in commands:
    run_command(cmd)
    Control the LED and update the OLED display with its status.
