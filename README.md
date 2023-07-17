# dots-files
My Archlinux dots file

## TODO:

Alacritty: improve padding + overall conf (theme)

Qtile: improve dmenu and status bar style, add focused border on full screen window

Add dots files that are not in .config


Why Qtile ? Cuz Python comfy

Why Alacritty ? Out of all the terminals I tried it's the one with the least delay for redrawing screen after moving window

nct6687 install DKMS : https://github.com/Fred78290/nct6687d
modbprobe.d options :
options kvm_intel nested=1
blacklist nct6683

module.load :
i2c_dev
nct6687


## Scripts: 
Folder is in the path. 

### record
record screenNumber fps.
Record screen at desired framerate, default to 25fps is no fps is specified. Output file is ~/Vidéos/screen.mp4.
Screen number is 1 or 2.

### sc

Screen capture the selection. Gets saved in ~/Images/screen.png


### brightness

Takes a number ranging from 0 to 100 to set hardware luminosity through ddcutil and redshift.
If the number is 0 then a low-blue light filter will be applied, if it's 100 it will be removed.

### tmux-sessionizer

Used through the shortcut ctrl+t in zsh.
Opens up a fuzzyfinder menu to select a folder that will open OR attach a tmux session in that folder.

Credits to ThePrimeagen: https://github.com/ThePrimeagen/.dotfiles/blob/master/bin/.local/scripts/tmux-sessionizer

## Software infos and shortcuts
### Tmux:

Shortcuts:
- leader + k : delete current session without prompt
- leader + n or o : go to next or previous session
- leader + s : list all sessions menu

### Qtile: 

Reload config from terminal if broken: qtile cmd-obj -o cmd -f reload_config

Shortcuts:
- mod + v or r : demenu_run
- mod + neoi : change windows focus colemak-vim style
- mod + ctrl + neoi : change windows size
- mod + shift + neoi: change windows position
- mod + alt + n or o : swap focused column to left or right
- mod + m : change screen focus
- mod + luy, : change virtual desktop of focused screen
- mod + shift + luy, : send focused windows to selected desktop
- mod + return : open new terminal window
- mod + w : kill window

### Alacritty:

Shorcuts:
- ctrl + shift + space : enter alacritty vi-mode, allows previous stdout selection vi-style
- ctrl + - or = : change zoom

In vi mode, we need to select with v before yanking, and we need to paste with system wide paste.

### Discord :

Shortcuts : 
- ctrl + t : open a sorta fzf menu to go to channels
- esc : scroll to end of conv

List of packages for the rice:

System packages:
- redshift (blue light filter)
- alacritty
- qtile
- dmenu
- tmux
- zsh
- ohmyzsh
- powerlevel10k
- neovim
- fzf

Python packages:
- grip (md viewer)
