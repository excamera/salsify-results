#!/bin/bash

# Clear rbenv variables before starting tmux
unset RBENV_VERSION
unset RBENV_DIR

tmux start-server;

  cd /home/sadjad/projects/salsify-results

  # Run pre command.
  

  # Create the session and the first window. Manually switch to root
  # directory if required to support tmux < 1.9
  TMUX= tmux new-session -d -s captain-eo -n experiment
  tmux send-keys -t captain-eo:0 cd\ /home/sadjad/projects/salsify-results C-m


  # Create other windows.


  # Window "experiment"
  tmux send-keys -t captain-eo:0.0 sudo\ su C-m
  tmux send-keys -t captain-eo:0.0 echo\ \"Capture\" C-m

  tmux splitw -c /home/sadjad/projects/salsify-results -t captain-eo:0
  tmux select-layout -t captain-eo:0 tiled
  tmux send-keys -t captain-eo:0.1 sudo\ su C-m
  tmux send-keys -t captain-eo:0.1 echo\ \"Playback\" C-m

  tmux splitw -c /home/sadjad/projects/salsify-results -t captain-eo:0
  tmux select-layout -t captain-eo:0 tiled
  tmux send-keys -t captain-eo:0.2 sudo\ su C-m
  tmux send-keys -t captain-eo:0.2 iotop C-m

  tmux splitw -c /home/sadjad/projects/salsify-results -t captain-eo:0
  tmux select-layout -t captain-eo:0 tiled
  tmux send-keys -t captain-eo:0.3 sudo\ su C-m
  tmux send-keys -t captain-eo:0.3 top C-m

  tmux select-layout -t captain-eo:0 tiled

  tmux select-layout -t captain-eo:0 tiled
  tmux select-pane -t captain-eo:0.0


  tmux select-window -t 0
  tmux select-pane -t 0

  if [ -z "$TMUX" ]; then
    tmux -u attach-session -t captain-eo
  else
    tmux -u switch-client -t captain-eo
  fi


