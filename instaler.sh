#!/bin/bash
sudo apt update 
mkdir /opt/translator
cp main.py /opt/translator
sudo chmod 777 trans
cp trans /usr/local/bin
if ls /usr/bin | grep -q "python3.12"; then
    :
else
    sudo apt install python3.12 -y
    sudo apt install python3-venv -y
fi

python3.12 -m venv /opt/translator/venv
