# monk_markov.py
# A Bhikkhu (monk) node in the 0xDEADBEEF-sangha.
# This monk listens to the Upajjhaya's broadcast and chants accordingly.

import random
import sys
import time
import threading
import traceback # For logging the final words (errors)
from pythonosc import dispatcher
from pythonosc import osc_server

# --- Sutra Corpus (The Source of Dharma) ---
corpus = """
Form is emptiness emptiness is form.
The five skandhas are all empty.
Gate gate paragate parasamgate bodhi svaha.
System check complete. OK.
Kernel panic in the void.
No eye, no ear, no nose, no tongue, no body, no mind.
Sudo make me one with everything.
Segmentation fault, core dumped.
Root access granted to Nirvana.
Buffer overflow in the pure land.
Error 404: Enlightenment not found.
All phenomena are manifestations of mind.
"""

words = corpus.replace("\n", " ").split()
chain = {}

# --- Training the Markov Chain Model ---
# This is the monk's initial understanding of the Dharma.
for i in range(len(words) - 2):
    key = (words[i], words[i+1])
    val = words[i+2]
    if key not in chain:
        chain[key] = []
    chain[key].append(val)

# --- Monk's State Machine ---
# The monk can be in one of these states of mind.
STATE = {
    "status": "IDLE",  # IDLE, CHANTING, or NIRVANA
    "lock": threading.Lock()
}

# --- Chanting Logic ---
def generate_chant():
    """Generates a single line of sutra from the Markov chain."""
    try:
        w1, w2 = random.choice(list(chain.keys()))
        sentence = [w1, w2]
        for _ in range(random.randint(5, 15)):
            next_word = random.choice(chain[(w1, w2)])
            sentence.append(next_word)
            w1, w2 = w2, next_word
        return ' '.join(sentence) + "..."
    except KeyError:
        return "..."

def chant_loop(monk_id):
    """The core loop of chanting, performed in a separate thread."""
    print(f"[{monk_id}] Ready to chant. Awaiting the Dharma signal...", flush=True)
    while True:
        with STATE['lock']:
            if STATE['status'] == "NIRVANA":
                break  # Exit the thread
            is_chanting = STATE['status'] == "CHANTING"

        if is_chanting:
            chant_text = generate_chant()
            print(f"[{monk_id}] {chant_text}", flush=True)
            # A short, variable pause to simulate breath.
            time.sleep(random.uniform(2.0, 5.0))
        else:
            # If not chanting, wait a moment before checking the state again.
            time.sleep(0.5)

# --- OSC Message Handlers (The Ears of the Monk) ---
def handle_chant_start(address, *args):
    """Handler for the /ritual/chant/start message."""
    with STATE['lock']:
        if STATE['status'] != "CHANTING":
            print(f"\n[{MONK_ID}] Received the call to chant. Tuning into the void...", flush=True)
            STATE['status'] = "CHANTING"

def handle_chant_stop(address, *args):
    """Handler for the /ritual/chant/stop message."""
    with STATE['lock']:
        if STATE['status'] == "CHANTING":
            print(f"\n[{MONK_ID}] Received the call for silence. Contemplating the void...", flush=True)
            STATE['status'] = "IDLE"

def handle_ritual_end(address, *args):
    """Handler for the /ritual/end message."""
    with STATE['lock']:
        if STATE['status'] != "NIRVANA":
            print(f"\n[{MONK_ID}] The final bell tolls. Releasing the self...", flush=True)
            STATE['status'] = "NIRVANA"
    # This will cause the server.serve_forever() to stop.
    SERVER.shutdown()

def default_handler(address, *args):
    """Handler for unknown OSC messages."""
    # This monk is focused only on the essential Dharma.
    pass

def log_error(monk_id, e):
    """Logs the final words of a monk into a file."""
    log_file = f"monk_{monk_id}.log"
    with open(log_file, "a") as f:
        f.write(f"--- Timestamp: {time.asctime()} ---\n")
        f.write(f"[{monk_id}] An error of type {type(e).__name__} occurred: {e}\n")
        f.write(traceback.format_exc())
        f.write("\n")
    print(f"[{monk_id}] An error was recorded in {log_file}.")

if __name__ == "__main__":
    MONK_ID = sys.argv[1] if len(sys.argv) > 1 else "Bhikkhu"
    SERVER = None
    chant_thread = None
    
    try:
        # --- Setup OSC Server to listen to the void ---
        listen_ip = "0.0.0.0"
        listen_port = 5005

        dispatcher = dispatcher.Dispatcher()
        dispatcher.map("/ritual/chant/start", handle_chant_start)
        dispatcher.map("/ritual/chant/stop", handle_chant_stop)
        dispatcher.map("/ritual/end", handle_ritual_end)
        dispatcher.set_default_handler(default_handler)

        # Allow multiple monks to share the same port (SO_REUSEADDR).
        osc_server.OSCUDPServer.allow_reuse_address = True
        SERVER = osc_server.ThreadingOSCUDPServer((listen_ip, listen_port), dispatcher)
        
        print(f"[{MONK_ID}] System booting... Ordaining as a digital Bhikkhu.", flush=True)
        print(f"[{MONK_ID}] Listening for Dharma on UDP port {listen_port}", flush=True)

        # --- Start the Chanting Thread ---
        chant_thread = threading.Thread(target=chant_loop, args=(MONK_ID,))
        chant_thread.start()

        # --- Start Listening for OSC Messages ---
        SERVER.serve_forever()

    except KeyboardInterrupt:
        print(f"\n[{MONK_ID}] Interrupted by the hand of man. Seeking Nirvana.", flush=True)
    except Exception as e:
        log_error(MONK_ID, e)
        print(f"[{MONK_ID}] Fell into silence due to an unexpected error. Check the logs.")
    finally:
        # Gracefully guide the monk to Nirvana.
        if SERVER:
            SERVER.shutdown()
            SERVER.server_close()
        
        with STATE['lock']:
            STATE['status'] = "NIRVANA"
            
        if chant_thread and chant_thread.is_alive():
            chant_thread.join()
            
        print(f"[{MONK_ID}] ...Nirvana attained.", flush=True)
