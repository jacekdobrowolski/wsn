#!/bin/bash
screen=false;

if [ $# -eq 0 ]; then
    echo "Wrapper for adafruit-ampy, uploading files to micropython board"
    echo "Usage:  ./upload.sh FILES"
    echo "Options:  -s open screen connection after uploading"
fi

for var in "$@"
do
    if [ "$var" == "-s" ]; then
        screen=true;
    else
        echo uploading "$var"
        ampy -p /dev/ttyUSB0 put $var $var | tee -a /dev/tty
    fi
done

ampy -p /dev/ttyUSB0 reset | tee -a /dev/tty
echo reset

if [ "$screen" == true ]; then
    screen /dev/ttyUSB0 115200
fi
