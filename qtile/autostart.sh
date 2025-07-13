#!/bin/sh
#picom &
imwheel &
#xrandr --output HDMI-0 --primary
/usr/bin/dunst &
#xrandr --output DP-2 --right-of HDMI-0 &
# xrandr --output DP-2 --rate 180 --mode 2560x1440 &
xrandr --output HDMI-0 --rate 120 --mode 3840x2160 &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
sleep 120
sshfs a.nixos:/etc/nixos ~/Documents/nixos &
