# Python Keylogger and Server

This project consists of two Python scripts:

1. `keylogger.py`: A Python keylogger that uses the `pynput` library to monitor keystrokes and sends them to a specified server over HTTP.
2. `server.py`: A simple Flask server that receives the keystrokes and writes them to a text file.

## Disclaimer

**These scripts are for educational purposes only.** Please use them responsibly and ensure you comply with all local and international laws. It's generally illegal and unethical to log keystrokes without informed consent.

## Requirements

- Python 3.6 or later
- `pynput` library for the keylogger script
- `requests` library for the keylogger script
- `flask` library for the server script

You can install the required libraries using pip:

```bash
pip install pynput requests flask
```

## Usage

### Keylogger

Update the `url` variable in `keylogger.py` with the URL of your server, then run the script on the computer you wish to monitor:

```bash
python keylogger.py
```

### Server

Run the server script on the computer that will receive the keystrokes:

```bash
python server.py
```

By default, the server will listen on all interfaces (`0.0.0.0`) on port `8080`. It will write received keystrokes to a file named `log.txt`.

## Security

These scripts do not implement any form of encryption, authentication, or error handling. In a real-world scenario, you should:

1. Use HTTPS to encrypt data transmission.
2. Authenticate the client sending the data.
3. Implement proper error handling and potentially rate-limiting to protect against abuse.
```

Please ensure you modify this README to accurately reflect any changes you make to the scripts.