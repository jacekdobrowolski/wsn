#!/bin/bash

ports=( "/dev/ttyUSB0" "/dev/ttyUSB1")

if [ $# -eq 0 ]; then
    echo "Wrapper for adafruit-ampy, uploading files to micropython board"
    echo "Usage:  ./upload.sh FILES"
    echo "Options:  -s open screen connection after uploading"
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
        echo "waiting for $port ${pids[$port]}"
        wait ${pids[$port]}
    done
done
