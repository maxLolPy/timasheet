#!/bin/bash
sudo apt update --fix-missing
sudo apt upgrade
sudo apt install python3-pip
sudo pip3 install camelot-py[cv]

