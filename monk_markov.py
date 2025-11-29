import random
import sys
import time

# --- Sutra Corpus ---
corpus = """
Form is emptiness emptiness is form
The five skandhas are empty
Gate gate paragate parasamgate bodhi svaha
System check complete OK
Kernel panic in the void
No eye no ear no nose no tongue
Sudo make me one with everything
Segmentation fault core dumped
Root access granted to Nirvana
Buffer overflow in the pure land
Error 404 Enlightenment not found
"""

words = corpus.replace("\n", " ").split()
chain = {}

# --- Training ---
for i in range(len(words) - 2):
    key = (words[i], words[i+1])
    val = words[i+2]
    if key not in chain:
        chain[key] = []
    chain[key].append(val)

# --- Chanting ---
def chant(monk_id):
    print(f"[{monk_id}] System booting... Connecting to void...", flush=True)
    time.sleep(2)

    while True:
        try:
            w1, w2 = random.choice(list(chain.keys()))
            sentence = [w1, w2]
            for _ in range(random.randint(5, 15)):
                next_word = random.choice(chain[(w1, w2)])
                sentence.append(next_word)
                w1, w2 = w2, next_word
        except KeyError:
            pass

        print(f"[{monk_id}] {' '.join(sentence)} ...", flush=True)
        
        if monk_id == "ProBook":
            sleep_time = random.uniform(1.0, 3.0)
        else:
            sleep_time = random.uniform(2.0, 5.0)
            
        time.sleep(sleep_time)

if __name__ == "__main__":
    monk_id = sys.argv[1] if len(sys.argv) > 1 else "S50"
    chant(monk_id)
