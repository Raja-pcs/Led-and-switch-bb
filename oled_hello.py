import subprocess

def run_command(command):
    """
    Run a shell command and print its output or error.
    """
    try:
        print(f"Running command: {command}")
        # Capture the output and errors
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error while running command: {e.stderr}")

# List of commands to run
commands = [
    "./oled_bin -n 2 -I 128x64",  # ① Initialize 128x64 resolution
    # "./oled_bin -n 2 -I 128x32",  # ② Initialize 128x32 resolution (commented out)
    "./oled_bin -n 2 -c",         # ③ Clear the display
    "./oled_bin -n 2 -r 0",       # ④ Rotate the display (0 degrees)
    "./oled_bin -n 2 -x 1 -y 1",  # ⑤ Set coordinates (example: x=1, y=1)
    "./oled_bin -n 2 -l \"Hello World!!!!\""  # ⑥ Display the string "Hello World!!!!"
]

# Run each command in sequence
for cmd in commands:
    run_command(cmd)

