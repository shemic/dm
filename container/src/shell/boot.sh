#!/bin/sh

set -e
set -u

if [ "$(ls /boot/)" ]; then
  for init in /boot/*.sh; do
    . $init
  done
fi