#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
# wallpaper
feh --bg-scale ~/cyber.png  

# opacitividad
picom --backend glx &

picom &
# lenguage
setxkbmap latam & 
picom --backend glx --window-shader-fg /usr/include/libplacebo/shaders/file.glsl &
