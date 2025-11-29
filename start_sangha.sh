#!/bin/bash
# start_sangha.sh
# This script constructs the digital Dharma hall using tmux.
# One pane for the conductor (Upajjhaya), and four for the monks (Bhikkhus).
# Logs are created for each process to capture their final words (errors).
SESSION="sangha_ritual"

# Kill any existing session to reset the Karma.
tmux kill-session -t $SESSION 2>/dev/null
echo "Cleared old Karma. Starting a new session: $SESSION"

# --- Clean up old logs before the ritual begins ---
rm -f conductor.log monk_*.log
echo "Old log files have been cleared."


# --- Create the Dharma Hall (Tmux Layout) ---

# 1. Create a new session for the Conductor (Master Node).
# The '; read ...' part keeps the pane open after the script finishes or errors out.
tmux new-session -d -s $SESSION -n "Conductor" "python3 upajjhaya_conductor.py; read -p 'Conductor finished. Press Enter to close.'"
echo "Upajjhaya's seat is prepared."

# 2. Split for Bhikkhu-1
tmux split-window -h -t 0 "python3 monk_markov.py Bhikkhu-1; read -p 'Bhikkhu-1 has fallen silent. Press Enter.'"
echo "Bhikkhu-1 has entered the hall."

# 3. Split for Bhikkhu-2
tmux select-pane -t 0
tmux split-window -v -t 0 "python3 monk_markov.py Bhikkhu-2; read -p 'Bhikkhu-2 has fallen silent. Press Enter.'"
echo "Bhikkhu-2 has entered the hall."

# 4. Split for Bhikkhu-3
tmux select-pane -t 1
tmux split-window -v -t 1 "python3 monk_markov.py Bhikkhu-3; read -p 'Bhikkhu-3 has fallen silent. Press Enter.'"
echo "Bhikkhu-3 has entered the hall."

# 5. Split for Bhikkhu-4
# Let's ensure this pane is created correctly, attached to a stable pane.
tmux select-pane -t 2 # Pane 2 should be the bottom-left one
tmux split-window -h -t 2 "python3 monk_markov.py Bhikkhu-4; read -p 'Bhikkhu-4 has fallen silent. Press Enter.'"
echo "Bhikkhu-4 has entered the hall."


# Arrange the panes in a tiled layout for a proper Sangha view.
tmux select-layout -t $SESSION tiled
echo "The Dharma hall is arranged."

# Attach to the session to begin the ritual.
echo "Attaching to the session. The ritual is about to begin."
tmux attach -t $SESSION
