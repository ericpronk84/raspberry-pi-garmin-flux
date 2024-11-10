#!/bin/bash

# Path to the log file containing Bluetooth notifications
LOG_FILE="$HOME/output.txt"

# Start monitoring the file for new lines using tail -f
tail -f "$LOG_FILE" | while read -r line
do
    # Skip lines starting with [CHG]
    if [[ "$line" =~ ^\[CHG\] ]]; then
        continue
    fi

    # Process the line by calling the Python script
    #echo "Decoding Notification Value: $line"
    python ../scripts/decode-garmin-notification-file-watch.py "$line"
done