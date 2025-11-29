#!/bin/bash
SESSION="sangha_sim"

# すでにセッションがあれば殺して再起動（リセット）
tmux kill-session -t $SESSION 2>/dev/null

# 1. 新規セッション作成 (左上: ProBook役)
# 少し早口な設定で起動
tmux new-session -d -s $SESSION -n "DigitalHall" "python3 monk_markov.py ProBook"

# 2. 画面分割 (右上: S50-1)
tmux split-window -h -t $SESSION "python3 monk_markov.py S50-1"

# 3. 画面分割 (左下: S50-2)
tmux split-window -v -t $SESSION "python3 monk_markov.py S50-2"

# 4. 画面分割 (右下: S50-3)
# まず右上のペイン(1番)を選択してから分割
tmux select-pane -t 1
tmux split-window -v -t $SESSION "python3 monk_markov.py S50-3"

# 5. レイアウトを「タイル状」に整列
tmux select-layout -t $SESSION tiled

# 6. セッションに接続（儀式開始）
tmux attach -t $SESSION

