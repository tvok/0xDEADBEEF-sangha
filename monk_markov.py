経 (Chanting) ---
def chant(monk_id):
    print(f"[{monk_id}] System booting... Connecting to void...", flush=True)
    time.sleep(2) # 起動演出

    while True: # 無限ループ
        try:
            # ランダムな開始地点を選ぶ
            w1, w2 = random.choice(list(chain.keys()))
            sentence = [w1, w2]
            
            # 1文の長さをランダムに決める (5〜15単語)
            for _ in range(random.randint(5, 15)):
                next_word = random.choice(chain[(w1, w2)])
                sentence.append(next_word)
                w1, w2 = w2, next_word
        except KeyError:
            pass # 文脈が途切れたら次の句へ

        # 生成された経文を出力
        # flush=True にしないとTmux等でリアルタイムに表示されないことがある
        print(f"[{monk_id}] {' '.join(sentence)} ...", flush=True)
        
        # 僧侶ごとの個性（リズム）
    import random
import sys
import time

# --- 経典コーパス (Sutra Corpus) ---
# 般若心経の英訳、Sanskrit、そしてLinuxのシステムログを混在させたもの
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

# --- 学習 (Training) ---
# 3-gram (2単語から次の1単語を予測) で連鎖を作る
for i in range(len(words) - 2):
    key = (words[i], words[i+1])
    val = words[i+2]
    if key not in chain:
        chain[key] = []
    chain[key].append(val)

# --- 読    # ProBookは早口、S50は処理落ちして遅い
        if monk_id == "ProBook":
            sleep_time = random.uniform(1.0, 3.0)
        else:
            sleep_time = random.uniform(2.0, 5.0)
            
        time.sleep(sleep_time)

if __name__ == "__main__":
    # 引数で名前を受け取る（なければ 'S50'）
    monk_id = sys.argv[1] if len(sys.argv) > 1 else "S50"
    chant(monk_id)

