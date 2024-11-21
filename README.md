# qtile-cyberpunk

Despues de instalar un archlinux limpio ( archinstall ) 

## Descargas dependencias :
- Descargamos algunos paquetes utiles 
```
sudo pacman -S xorg git firefox code kitty feh picom dmenu fish 
```
- Instalar qtile
```
sudo pacaman -S qtile
```
- Descargamos el AUR ( **[yay](https://github.com/Jguer/yay?tab=readme-ov-file)** )
```
sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
```

- Clonar mi repositorio y moverlo como .config a tu sistema : 
```
git clone https://github.com/cristhian-bot0/qtile_hacker.git
```

Cambiar el shell con el comando **[chsh](https://www.ochobitshacenunbyte.com/2020/03/02/cambiar-la-shell-de-un-usuario-en-linux-con-chsh/)** `chsh -s /bin/fish $user$` 


3. Descargamos las nerd fonts , opcion 64. 
```
yay -S nerd-fonts 
```


Test it with **[Xephyr](https://github.com/cristhian-bot0/qtile.git)**:


If the network widget doesn't work check ```./settings/widgets.py``` and look
for this line, you should find it inside a list called *primary_widgets*:

```python
# Change interface arg, use ip address to find which one you need
 widget.Net(**base(bg='color3'), interface='wlp2s0'),
```


## Structure

In ```config.py```, which is the file where most people write all their config,
I only have an *autostart* function and some other variables like
*cursor_warp*.

```python
@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])
```

If you want to change *autostart* programs, open  ```./autostart.sh```.

```bash
#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
```

## Themes

To set a theme, check which ones are available in ```./themes```, and write
the name of the theme you want in a file named ```./config.json```:

```json
{
    {"theme": "metal-dark"}

}
··

##  app-adittional

acpi -> mirar el porcentaje de la bateria
**[picom](https://wiki.archlinux.org/title/Picom)** -> para la opacidad de ventanas



