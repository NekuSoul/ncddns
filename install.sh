#!/usr/bin/env bash

if ! [[ $(id -u) = 0 ]]; then
   echo "This script requires root!"
   exit 1
fi

mkdir -p /opt/ncddns
cp *.py /opt/ncddns/
cp ncddns.conf.example /opt/ncddns/ncddns.conf.example