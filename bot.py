#!/usr/bin/env python3
"""
Meshtastic Basic Bot
A simple auto-reply bot that responds with 'ok' to any direct message.

This is a minimal starting point for building Meshtastic bot functionality.
"""

import sys
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional
from pubsub import pub

# Try importing meshtastic interfaces
try:
    import meshtastic
    import meshtastic.serial_interface
    import meshtastic.tcp_interface
    import meshtastic.ble_interface
except ImportError:
    print("ERROR: Meshtastic library not installed!")
    print("Install with: pip install meshtastic")
    sys.exit(1)


class MeshtasticBasicBot:
    """Basic bot that responds with 'ok' to direct messages"""

    def __init__(self, reply_message: str = "ok"):
        self.reply_message = reply_message
        self.interface: Optional[meshtastic.serial_interface.SerialInterface] = None
        self.setup_logging()

    def setup_logging(self):
        """Configure logging to file and console"""
        log_file = Path('logs') / f'bot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        log_file.parent.mkdir(exist_ok=True)

        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("Bot initialized")
        self.logger.info(f"Reply message: '{self.reply_message}'")

    def connect(self, connection_type: str, address: Optional[str] = None) -> bool:
        """
        Connect to Meshtastic node

        Args:
            connection_type: 'serial', 'tcp', or 'ble'
            address: Port/IP/MAC address (None for auto-detect on BLE)
        """
        try:
            self.logger.info(f"Connecting via {connection_type}...")

            if connection_type == 'serial':
                if not address:
                    raise ValueError("Serial port required (e.g., COM3 or /dev/ttyUSB0)")
                self.interface = meshtastic.serial_interface.SerialInterface(address)

            elif connection_type == 'tcp':
                if not address:
                    raise ValueError("IP address required (e.g., 192.168.1.100)")
                self.interface = meshtastic.tcp_interface.TCPInterface(hostname=address)

            elif connection_type == 'ble':
                # BLE can auto-discover or use specific MAC
                if address:
                    self.interface = meshtastic.ble_interface.BLEInterface(address)
                else:
                    self.interface = meshtastic.ble_interface.BLEInterface()
            else:
                raise ValueError(f"Unknown connection type: {connection_type}")

            self.logger.info("Connected successfully!")
            return True

        except Exception as e:
            self.logger.error(f"Connection failed: {e}")
            return False

    def on_receive(self, packet, interface):
        """Handle received messages"""
        try:
            # Check if it's a message we should handle
            if 'decoded' not in packet:
                return

            decoded = packet['decoded']

            # Only handle text messages
            if 'text' not in decoded:
                return

            message_text = decoded['text'].strip()
            sender_id = packet['from']
            to_id = packet.get('to', 0)

            # Get sender info for logging
            sender_info = f"Node {sender_id:08x}"
            if 'fromId' in packet:
                sender_info = packet['fromId']

            # Check if it's a direct message to us (not broadcast)
            is_direct_message = to_id != 0xffffffff

            self.logger.info(f"Message from {sender_info}: '{message_text}' (Direct: {is_direct_message})")

            # Only respond to direct messages
            if not is_direct_message:
                self.logger.debug("Ignoring broadcast message")
                return

            # Send the reply
            self.send_reply(sender_id, self.reply_message, sender_info)

        except Exception as e:
            self.logger.error(f"Error handling message: {e}", exc_info=True)

    def send_reply(self, destination_id: int, message: str, recipient_info: str):
        """Send a reply message"""
        try:
            self.interface.sendText(message, destinationId=destination_id)
            self.logger.info(f"Sent to {recipient_info}: '{message}'")
        except Exception as e:
            self.logger.error(f"Failed to send reply: {e}")

    def start(self):
        """Start the bot and listen for messages"""
        if not self.interface:
            self.logger.error("Not connected! Call connect() first.")
            return

        # Subscribe to message events
        pub.subscribe(self.on_receive, "meshtastic.receive")

        self.logger.info("Bot started! Monitoring for direct messages...")
        self.logger.info("Press Ctrl+C to stop")

        # Keep running
        try:
            while True:
                import time
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.logger.info("\nBot stopped by user")
            self.stop()

    def stop(self):
        """Clean shutdown"""
        if self.interface:
            self.interface.close()
        self.logger.info("Connection closed")


def get_connection_settings() -> tuple:
    """Interactive prompt for connection settings"""
    print("\n" + "="*50)
    print("  MESHTASTIC BASIC BOT")
    print("="*50)
    print("\nSelect connection type:")
    print("  1. USB/Serial (most reliable)")
    print("  2. WiFi/TCP (requires WiFi-enabled node)")
    print("  3. Bluetooth/BLE (wireless, short range)")
    print()

    while True:
        choice = input("Enter choice (1-3): ").strip()

        if choice == '1':
            print("\nExamples: COM3 (Windows), /dev/ttyUSB0 (Linux), /dev/cu.usbserial (Mac)")
            port = input("Enter serial port: ").strip()
            if port:
                return ('serial', port)

        elif choice == '2':
            print("\nEnter node's IP address (e.g., 192.168.1.100)")
            ip = input("IP address: ").strip()
            if ip:
                return ('tcp', ip)

        elif choice == '3':
            print("\nLeave blank for auto-discovery or enter MAC address")
            mac = input("MAC address (optional): ").strip()
            return ('ble', mac if mac else None)

        print("Invalid choice or empty input. Try again.\n")


def main():
    """Main entry point"""

    print("\nMeshtastic Basic Bot - Responds with 'ok' to all direct messages")
    print("="*60)

    # Optional: customize reply message
    custom = input("\nUse default reply 'ok'? (Y/n): ").strip().lower()
    if custom == 'n':
        reply_msg = input("Enter custom reply message: ").strip()
        if not reply_msg:
            reply_msg = "ok"
    else:
        reply_msg = "ok"

    # Get connection settings
    conn_type, address = get_connection_settings()

    # Create and connect bot
    bot = MeshtasticBasicBot(reply_message=reply_msg)

    if bot.connect(conn_type, address):
        bot.start()
    else:
        print("\nFailed to connect. Check settings and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()
