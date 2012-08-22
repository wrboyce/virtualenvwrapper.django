#!/bin/sh


echo "Activating sudo NOPASSWD for admin users..."
sed -i 's/%admin ALL=(ALL) ALL/%admin ALL=(ALL) NOPASSWD:ALL/' /etc/sudoers

apt-get update
apt-get upgrade -yqq

GENERAL_PACKAGES="zsh zsh-doc git git-doc vim vim-doc screen curl"
MONITORING_PACKAGES="sysstat htop iotop iftop"
SERVER_PACKAGES="postgresql nginx"
PYTHON_PACKAGES="python2.7 python-setuptools"
apt-get install -yqq $GENERAL_PACKAGES $MONITORING_PACKAGES $SERVER_PACKAGES $PYTHON_PACKAGES
easy_install pip
pip install virtualenv virtualenvwrapper

apt-get dist-upgrade -yqq
reboot
