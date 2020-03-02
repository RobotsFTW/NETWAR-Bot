#!/bin/bash

#try to restart it 10 times immediately, if it cant try every 5 minutes for an hour.

FAILS=0
FAILS1=0

while true
do
  sleep 0.5
  python3 bot.py # your program
  EXIT=$?
  ((FAILS++))

  if [[ $FAILS -gt 10 ]]
  then
    echo "[$(date)] bot cannot be restarted now waiting 5 minutes"
         while true
         do
              sleep 0.5
              python3 bot.py # your program
              EXIT=$?
              ((FAILS1++))
              echo "[$(date) bot exited with code $EXIT. Restarting in 5 minutes"
              sleep 300

              if [[ $FAILS1 -gt 15 ]]
              then
                  echo "[$(date) Bot could not be reconnected in an hour exiting script."
                  exit 1
              fi
         done
    exit 1
  fi

  echo "[$(date)] bot exited with code $EXIT. restarting ..."

done
