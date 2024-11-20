# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.lazy import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    # Cambiar entre ventanas en el panel de pila actual

    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    # Cambiar el tamaño de las ventanas (MonadTall)

    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    # Cambiar a flotante 

    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    # Mover ventanas arriba o abajo en la pila actual
    
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    # Alternar entre diferentes diseños como se define a continuación

    ([mod], "Tab", lazy.next_layout()),
    ([mod], "t", lazy.window.toggle_fullscreen()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    # Eliminar vetana 

    ([mod], "w", lazy.window.kill()),

    # Switch focus of- monitors
    # Cambiar el enfoque de los monitores

    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    # Reiniciar Qtile 

    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    #Apagar 
    ([mod, "shift"], "p", lazy.spawn("shutdown now")),

    # ------------ App Configs ------------

    # Menu
    #([mod], "m", lazy.spawn("dmenu_run -b -i -fn \"Cantarell-15\" -nb \"#000000\" -nf \"#a06666\" -p \"start-app\" -sb \"#3F575B\"")),
    ([mod], "l", lazy.spawn("dmenu_run -b -i -fn \"Cantarell-18\" -nb \"#000000\" -nf \"#0ccdd7\" -p \"start-app\" -sb \"#d300c4\" -sf \"#181c52\"")),

    # Browser
    ([mod], "b", lazy.spawn("firefox")),

    # File Explorer
    ([mod], "e", lazy.spawn("pcmanfm")),

    # Terminal
    ([mod], "Return", lazy.spawn("kitty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot 'screenshot_%Y-%m-%d-%T_$wx$h.png' -e 'mkdir -p ~/images/screenshots/ | mv $f ~/images/screenshots/'")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),
    
    # Opacitividad 
    ([mod], "p", lazy.spawn("xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x1080 --output HDMI-1-1 --mode 1920x1080 --pos 0x0")), 

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
