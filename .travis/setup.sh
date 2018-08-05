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

# Avoid running privileged containers, cf. https://stgraber.org/2017/06/15/custom-user-mappings-in-lxd-containers/
sudo sed -i 's/^\(lxd:[0-9]\{1,\}\):.*/\1:1000000000/' /etc/subuid
sudo sed -i 's/^\(root:[0-9]\{1,\}\):.*/\1:1000000000/' /etc/subuid
sudo sed -i 's/^\(lxd:[0-9]\{1,\}\):.*/\1:1000000000/' /etc/subgid
sudo sed -i 's/^\(root:[0-9]\{1,\}\):.*/\1:1000000000/' /etc/subgid
cat /etc/subuid
cat /etc/subgid
sudo systemctl restart lxd
cat /etc/subuid
cat /etc/subgid

cat /var/log/lxd/lxd.log
