# Meshtastic-Reply-Bot
A python reply bot for meshtastic nodes - send any message and it replies 'ok'. 
I made it to help me range test my nodes.

This is a minimal starting point for building custom Meshtastic bot functionality. Future versions will include additional features based on community feedback.

Features
✅ Auto-reply with "ok" (or custom message) to direct messages
✅ Supports USB/Serial, WiFi/TCP, and Bluetooth connections
✅ Message logging to files and console
✅ Ignores broadcast messages (only responds to direct messages)
✅ Simple, clean codebase for learning and extending
Requirements
Python 3.8 or higher
Meshtastic node (any supported hardware)
Connection method: USB cable, WiFi network, or Bluetooth
Installation
Windows
Install Python (if not already installed):

Download from python.org
During installation, check "Add Python to PATH"
Clone or download this repository:

git clone https://github.com/benb0jangles/Meshtastic-Reply-Bot.git
cd Meshtastic-Reply-Bot
Install dependencies:

pip install -r requirements.txt
Connect your Meshtastic node:

USB: Plug in via USB cable
WiFi: Ensure node is on same network
Bluetooth: Turn on Bluetooth on your PC
Linux
Install Python (usually pre-installed):

# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Fedora/RHEL
sudo dnf install python3 python3-pip

# Arch
sudo pacman -S python python-pip
Clone or download this repository:

git clone https://github.com/benb0jangles/Meshtastic-Reply-Bot.git
cd Meshtastic-Reply-Bot
Install dependencies:

pip3 install -r requirements.txt
Add user to dialout group (for USB access):

sudo usermod -a -G dialout $USER
# Log out and back in for changes to take effect
Connect your Meshtastic node:

USB: Plug in via USB cable (usually /dev/ttyUSB0 or /dev/ttyACM0)
WiFi: Ensure node is on same network
Bluetooth: Ensure Bluetooth is enabled
Usage
Basic Usage
Run the bot with default settings:

# Windows
python bot.py

# Linux
python3 bot.py
The bot will:

Ask if you want to use the default "ok" reply (or customize it)
Prompt you to select a connection type
Connect to your Meshtastic node
Start monitoring for direct messages
Connection Types
1. USB/Serial (Most Reliable):

Windows: Usually COM3, COM4, etc.
Linux: Usually /dev/ttyUSB0 or /dev/ttyACM0
Mac: Usually /dev/cu.usbserial-*
To find your port:

# Windows (PowerShell)
Get-WmiObject Win32_SerialPort | Select-Object DeviceID, Description

# Linux
ls /dev/ttyUSB* /dev/ttyACM*

# Mac
ls /dev/cu.usbserial*
2. WiFi/TCP (Requires WiFi-enabled node):

Enter your node's IP address (e.g., 192.168.1.100)
Node must be configured in WiFi Client or AP mode
Check IP via Meshtastic app or CLI: meshtastic --host IP_ADDRESS --info
3. Bluetooth/BLE (Wireless, 5-10m range):

Leave blank for auto-discovery
Or enter specific MAC address (e.g., AA:BB:CC:DD:EE:FF)
Requires Python bleak library (included in dependencies)
Example Session
$ python3 bot.py

Meshtastic Basic Bot - Responds with 'ok' to all direct messages
================================================================

Use default reply 'ok'? (Y/n): y

==================================================
  MESHTASTIC BASIC BOT
==================================================

Select connection type:
  1. USB/Serial (most reliable)
  2. WiFi/TCP (requires WiFi-enabled node)
  3. Bluetooth/BLE (wireless, short range)

Enter choice (1-3): 1

Examples: COM3 (Windows), /dev/ttyUSB0 (Linux), /dev/cu.usbserial (Mac)
Enter serial port: /dev/ttyUSB0

2025-11-27 10:30:15 [INFO] Bot initialized
2025-11-27 10:30:15 [INFO] Reply message: 'ok'
2025-11-27 10:30:15 [INFO] Connecting via serial...
2025-11-27 10:30:17 [INFO] Connected successfully!
2025-11-27 10:30:17 [INFO] Bot started! Monitoring for direct messages...
2025-11-27 10:30:17 [INFO] Press Ctrl+C to stop
How It Works
Listens for messages: The bot monitors your Meshtastic node for incoming messages
Filters direct messages: Only responds to direct messages (not broadcasts)
Auto-reply: Sends "ok" (or your custom message) back to the sender
Logging: All activity is logged to console and logs/ directory
Customization
Change Reply Message
When starting the bot, you can customize the reply:

Use default reply 'ok'? (Y/n): n
Enter custom reply message: Roger that!
Extend Functionality
The code is designed to be simple and easy to extend. Future versions will include:

Command parsing (e.g., "!help", "!status")
Multiple response types
Scheduled messages
Data logging and analytics
Integration with external APIs
Stay tuned for updates!

Logs
All bot activity is logged to the logs/ directory:

File format: bot_YYYYMMDD_HHMMSS.log
Contains all received messages and sent replies
Useful for debugging and monitoring
Troubleshooting
"Meshtastic library not installed"
pip install meshtastic
# or
pip3 install meshtastic
"Permission denied" (Linux USB)
sudo usermod -a -G dialout $USER
# Then log out and back in
"Connection failed"
USB: Check port name, ensure node is connected and in bootloader mode if needed
WiFi: Verify IP address, ensure node WiFi is enabled and on same network
Bluetooth: Ensure Bluetooth is enabled on both devices, try auto-discovery
"No response from bot"
Make sure you're sending direct messages, not broadcasts
Check logs in logs/ directory for errors
Verify node is responding: meshtastic --port PORT --info
Contributing
This is a community project! Contributions welcome:

Report bugs via GitHub Issues
Suggest features for future versions
Submit pull requests with improvements
Roadmap
v1.0 (Current): Basic auto-reply with "ok"
v1.1 (Planned): Custom command support
v1.2 (Planned): Multiple response patterns
v1.3 (Planned): External API integration

License
MIT License - See LICENSE file for details

Resources
Meshtastic Official Docs
Meshtastic Python API
Meshtastic Discord
Author - Benb0jangles
Created as a learning project and starting point for Meshtastic bot development.

Found this useful? Star the repository and watch for updates!
