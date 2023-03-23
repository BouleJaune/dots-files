#!/bin/sh
#picom &
imwheel &
#xrandr --output HDMI-0 --left-of DP-0 &
xrandr --output DP-0 --left-of HDMI-0 &
xrandr --output DP-0 --primary &
