#!/bin/bash
# start_sangha.sh - A deterministic tmux launcher for the Sangha

SESSION="sangha_ritual"
PD_IP="127.0.0.1"
PD_PORT="3000"
WORKDIR="/Users/frost/digital_temple"

# Kill any existing session
tmux kill-session -t $SESSION &>/dev/null || true
sleep 1

echo "Configuring Dharma Hall..."

# Create a session with a single window.
tmux new-session -d -s $SESSION -c "$WORKDIR" -x 160 -y 40

# --- Create a deterministic 2x2 layout ---
# This creates pane 1 below pane 0
tmux split-window -v -c "$WORKDIR"
# Select the top pane (0) and split it horizontally. This creates pane 2 to the right.
tmux select-pane -t 0
tmux split-window -h -c "$WORKDIR"
# Select the bottom pane (1) and split it horizontally. This creates pane 3 to the right.
tmux select-pane -t 1
tmux split-window -h -c "$WORKDIR"

# Wait for all panes to be fully initialized
sleep 2

# --- Send commands to the well-defined panes ---
# Pane mapping after splits: 0=TL, 2=TR, 1=BL, 3=BR
PANE_CMD="python3 monk_markov.py"
PD_ARGS="--pd-enable --pd-ip $PD_IP --pd-port $PD_PORT"

# Use the full session:window.pane format for addressing and assign unique listen ports
tmux send-keys -t "${SESSION}:0.0" "$PANE_CMD Bhikkhu-1 $PD_ARGS --listen-port 5005" Enter # Top-Left
tmux send-keys -t "${SESSION}:0.2" "$PANE_CMD Bhikkhu-2 $PD_ARGS --listen-port 5006" Enter # Top-Right
tmux send-keys -t "${SESSION}:0.1" "$PANE_CMD Bhikkhu-3 $PD_ARGS --listen-port 5007" Enter # Bottom-Left
tmux send-keys -t "${SESSION}:0.3" "$PANE_CMD Bhikkhu-4 $PD_ARGS --listen-port 5008" Enter # Bottom-Right

echo "✓ 4 Bhikkhus summoned."
sleep 1

# Attach to the session
tmux attach -t $SESSION
