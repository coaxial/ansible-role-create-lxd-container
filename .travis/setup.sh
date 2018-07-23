#!/bin/sh
sudo apt-get update
# xenial ships LXD 2 LTS, backports ships 3 LTS
sudo apt-get upgrade -t xenial-backports -y lxd lxd-client

sudo lxd --version
# Wait for the socket to be ready
sudo lxd waitready
sudo lxd init --auto

pip install ansible
pip install molecule

# Avoid running privileged containers, cf. https://archive.fo/KhNgb
sudo sed -i 's/(lxd:.*):\d+/\1:1000000000' /etc/subuid
sudo sed -i 's/(root:.*):\d+/\1:1000000000' /etc/subuid
sudo sed -i 's/(lxd:.*):\d+/\1:1000000000' /etc/subgid
sudo sed -i 's/(root:.*):\d+/\1:1000000000' /etc/subgid
