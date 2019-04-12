#!/usr/bin/env bash

if ! [[ $(id -u) = 0 ]]; then
   echo "This script requires root!"
   exit 1
fi

cp ncddns.service /etc/systemd/system/ncddns.service
cp ncddns.timer /etc/systemd/system/ncddns.timer
systemctl daemon-reload
systemctl enable ncddns.timer
systemctl start ncddns.timer