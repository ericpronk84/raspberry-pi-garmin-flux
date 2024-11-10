#!/bin/bash

# Start monitoring Bluetooth notifications using bluetoothctl
bluetoothctl monitor | while read -r line
do
    # Filter for notifications related to Bluetooth attributes (Value)
    if [[ "$line" =~ "Value" ]]; then
        # If notification is received, run your Python script or any other action
        echo "Received Notification: $line"

        # Call Python script to process the notification
        python ../scripts/decode-garmin-notification-file-watch.py "$line"
    fi
done