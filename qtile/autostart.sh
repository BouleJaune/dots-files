#!/bin/sh
#picom &
imwheel &
#xrandr --output HDMI-0 --left-of DP-0 &
xrandr --output HDMI-0 --primary
xrandr --output DP-0 --right-of HDMI-0 &
sshfs nixos:/mnt/hdd ~/nixos_server &
