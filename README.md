# Keylogger 📜 README

## Overview 📚

This repository contains a simple keylogger that consists of a server and a client, allowing you to monitor and record keyboard input on a target machine. It's essential to use this software responsibly and only on systems you have explicit permission to monitor. Unauthorized use of keyloggers is illegal and unethical. 🔒

## Features 🌟

- The server 🖥️ listens for incoming connections and logs the received keystrokes.
- The client 💻 runs on the target machine and sends keystrokes to the server.
- Keystrokes are logged to a file 📝 on the client machine and transmitted to the server in real-time.
- The client and server communicate over a network 🌐, allowing remote monitoring.

## Usage 🚀

1. **Server Setup**:
   - Run the server script on a machine where you want to collect keystroke data.
   - The server listens for incoming connections on the specified IP address and port.

2. **Client Setup**:
   - Replace `'SERVER_IP'` in the client script with the IP address of your server.
   - Run the client script on the target machine where you want to monitor keystrokes.
   - The client logs keystrokes to a file (key_strokes.txt) and sends them to the server.

3. **Monitoring**:
   - The server will display received keystrokes in its console.
   - Keystrokes are also logged to a file on the client machine (key_strokes.txt).

## Important Notes ⚠️

- This keylogger should be used responsibly and legally. Unauthorized use is a violation of privacy and may be illegal.
- Respect local laws and obtain appropriate permissions before using this software.
- The code is provided for educational purposes only, and the authors are not responsible for any misuse.

## License 📝

This software is distributed under the following license:

**MIT License** 📄

