#!/bin/bash

ports=( "/dev/ttyUSB0" "/dev/ttyUSB1")

if [ $# -eq 0 ]; then
    echo "Wrapper for adafruit-ampy, uploading files to micropython board"
    echo "Usage:  ./upload.sh FILES"
fi

for var in "$@"
do
    declare -A pids
    for port in "${ports[@]}"; do
        echo "uploading $var to $port"
        ampy -p "$port" put "$var" "$var" | tee -a /dev/tty &
        pids[$port]="$!"
    done

    # wait for all pids
    for port in "${!pids[@]}"; do
        PID=${pids[$port]}
        echo "waiting for $port $PID"
        wait $PID
    done
done

 for port in "${ports[@]}"; do
        echo "reseting $port"
        ampy -p "$port" reset | tee -a /dev/tty &
done
