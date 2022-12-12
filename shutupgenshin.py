'Simple script for skipping dialogues in genshin.'
import json
import time
import threading
import pydirectinput
from pynput.keyboard import Listener


def clicker(config):
    'Main clicker function.'
    while True:
        if not PAUSED:
            pydirectinput.moveTo(int(config['x_coordinates']), int(config['y_coordinates']))
            pydirectinput.click()
        time.sleep(float(config['press_timer']))


def pause(key, keybind):
    'Pause.'
    global PAUSED
    if keybind in str(key):
        PAUSED = not PAUSED
        print("[INFO] Condition swapped.")


def get_settings(path='settings.json'):
    'Gets configuration from settings file.'
    with open(path, 'r', encoding='utf8') as file:
        settings = json.load(file)
    return settings


if __name__ == '__main__':
    print("[INIT] STFUgenshin started.")
    print("\n[INFO] Dont forget to configure resolution in settings.json.")
    print("[INFO] Calibrated on 1920x1080 by default.")
    configuration = get_settings()
    PAUSED = True

    thread = threading.Thread(target=clicker, args=(configuration,))
    thread.start()

    with Listener(on_press=lambda event: \
        pause(event, keybind=str(configuration['start_pause_key']))) as listener:
        listener.join()
