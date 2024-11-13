from libqtile import widget
from libqtile.widget.battery import thunderbolt_smart_charge
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }
def powerline(fg="light", bg="black"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=37,
        padding=-2
    )
def separator6():
    return widget.Sep(**base(), linewidth=0, padding=300)
def separator8():
    return widget.Sep(**base(), linewidth=0, padding=720)
def separator2():
    return widget.Sep(**base(), linewidth=0, padding=30)
def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=30,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=1,
            highlight_method='line',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator6(),
        
    ]




primary_widgets = [
    separator2(),
    widget.Battery(
        format='{percent:2.0%} {char}',
        foreground=colors['color4'],
        charge_char='⚡',
        discharge_char='󰁿',
        fontshadow= None ,
        fontsize=25,
        width=80,  
    ),
#    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
    separator2(),
    
    widget.Clock(
        foreground=colors['color4'],
        format='%d/%m/%Y - %H:%M ',
        fontsize=18,
    ),
    separator6(),
    *workspaces(),
#    icon(bg="color4", text=' '), # Icon: nf-fa-download
#    icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    separator2(),
    widget.Battery(
        format='{percent:2.0%} {char}',
        foreground=colors['color4'],
        charge_char='⚡',
        discharge_char='󰁿',
        fontshadow= None ,
        fontsize=25,
        width=80,  
    ),
#    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
    separator2(),
    
    widget.Clock(
        foreground=colors['color4'],
        format='%d/%m/%Y - %H:%M ',
        fontsize=18,
    ),

    #widget.Systray(background=colors['dark'], padding=5),
    separator2(),
    separator2(),
]

secondary_widgets = [
    separator2(),
    widget.Battery(
        format='{percent:2.0%} {char}',
        foreground=colors['color4'],
        charge_char='⚡',
        discharge_char='󰁿',
        fontshadow= None ,
        fontsize=25,
        width=80,  
    ),
#    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
    separator2(),
    
    widget.Clock(
        foreground=colors['color4'],
        format='%d/%m/%Y - %H:%M ',
        fontsize=18,
    ),
    separator6(),
    *workspaces(),
#    icon(bg="color4", text=' '), # Icon: nf-fa-download
#    icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    separator2(),
    widget.Battery(
        format='{percent:2.0%} {char}',
        foreground=colors['color4'],
        charge_char='⚡',
        discharge_char='󰁿',
        fontshadow= None ,
        fontsize=25,
        width=80,  
    ),
#    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
    separator2(),
    
    widget.Clock(
        foreground=colors['color4'],
        format='%d/%m/%Y - %H:%M ',
        fontsize=18,
    ),

    #widget.Systray(background=colors['dark'], padding=5),
    separator2(),
    separator2(),
]
widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
