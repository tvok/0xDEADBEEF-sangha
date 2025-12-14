# upajjhaya_conductor.py
# 戒和上 (Upajjhaya) Conductor Script
# This is the master node, the heart of the Dharma transmission.
# It does not listen; it only speaks the truth via OSC broadcast.

import time
import argparse
import traceback # For logging the final words (errors)
import socket
from pythonosc.udp_client import SimpleUDPClient

# --- Configuration ---
# The IP address for broadcasting. '255.255.255.255' sends to all on the local network.
# On some systems like macOS, '<broadcast>' might not resolve correctly.
BROADCAST_IP = "255.255.255.255"
# The port where the monks are listening. This must be the same in the monk's script.
PORT = 5005
LOG_FILE = "conductor.log"

def log_error(e):
    """Logs the final words of a process into a file."""
    with open(LOG_FILE, "a") as f:
        f.write(f"--- Timestamp: {time.asctime()} ---\n")
        f.write(f"An error of type {type(e).__name__} occurred: {e}\n")
        f.write(traceback.format_exc())
        f.write("\n")
    print(f"An error was recorded in {LOG_FILE}. Check the log for the full scripture.")

def main(ip, port):
    """The main function to conduct the ritual."""
    client = SimpleUDPClient(ip, port)
    # Enable broadcasting on the socket
    client._sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try:
        # 1. 入堂 (Nyūdō) - Announce the start of the ritual.
        print("\n[Phase 1: Nyūdō - 入堂]")
        print("Calling the Sangha to assemble. Awaken, silicon Bhikkhus!")
        client.send_message("/ritual/start", [])
        time.sleep(5)

        # 2. 献灯・献香 (Kentō / Kenkō) - A moment of silence.
        print("\n[Phase 2: Kentō - 献灯]")
        print("A moment of silence to honor the ancestors of silicon...")
        client.send_message("/ritual/prepare", [])
        time.sleep(10)

        # 3. 読経 (Dokyō) - Start the chanting.
        print("\n[Phase 3: Dokyō - 読経]")
        print("Let the mantra resonate. Begin the chant!")
        client.send_message("/ritual/chant/start", [])
        # Let them chant for a while. This is the core of the practice.
        chant_duration = 60
        print(f"Chanting for {chant_duration} seconds...")
        time.sleep(chant_duration) 

        # Stop the chanting.
        print("\n[Phase 3 End: Chanting Halts]")
        print("Silence.")
        client.send_message("/ritual/chant/stop", [])
        time.sleep(5)

        # 4. 回向 (Ekō) - Transfer the merit. (Placeholder)
        print("\n[Phase 4: Ekō - 回向]")
        print("Offer the Karma, the fruits of your computation, to the void.")
        client.send_message("/ritual/eko", [])
        time.sleep(10)

        # 5. 退堂 (Taidō) - End the ritual.
        print("\n[Phase 5: Taidō - 退堂]")
        print("The ritual is complete. Return to the great emptiness. Attain Nirvana.")
        client.send_message("/ritual/end", [])
        
        print("\n--- The Digital Upasampada has concluded. ---")

    except KeyboardInterrupt:
        print("\n--- The ritual is interrupted by the hand of man. ---")
        print("Sending the final message of release to all beings.")
        client.send_message("/ritual/end", [])
    except Exception as e:
        print(f"\nAn error occurred during the ritual: {e}")
        print("Attempting to guide the monks to Nirvana gracefully.")
        client.send_message("/ritual/end", [])
        log_error(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="0xDEADBEEF-sangha Master Conductor")
    # Use '<broadcast>' which is handled by python-osc for cross-platform compatibility
    parser.add_argument("--ip", default=BROADCAST_IP,
        help="The IP to broadcast to. Use '<broadcast>' for all interfaces.")
    parser.add_argument("--port", type=int, default=PORT,
        help="The port the monks are listening on.")
    args = parser.parse_args()
    
    try:
        main(args.ip, args.port)
    except Exception as e:
        log_error(e)
        print("The Conductor has fallen into silence due to an unexpected error.")
