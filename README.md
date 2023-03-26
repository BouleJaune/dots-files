# dots-files
My Archlinux dots file

Scripts: 
Folder is in the path. 

brightness command helper:

Takes a number ranging from 0 to 100 to set hardware luminosity through ddcutil and redshift.
If the number is 0 then a low-blue light filter will be applied, if it's 100 it will be removed.

tmux-sessionizer command :

Used through the shortcut ctrl+t in zsh
Opens up a fuzzyfinder menu to select a folder that will open OR attach a tmux session in that folder
Credits to ThePrimeagen: https://github.com/ThePrimeagen/.dotfiles/blob/master/bin/.local/scripts/tmux-sessionizer

Tmux:

Shortcuts:
- leader + k : delete current session without prompt
- leader + n or o : go to next or previous session
- leader + s : list all sessions menu

Qtile: 

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

Alacritty:

Shorcuts:
- ctrl + shift + space : enter alacritty vi-mode, allows previous stdout selection vi-style
- ctrl + - or = : change zoom

In vi mode, we need to select with v before yanking, and we need to paste with system wide paste.


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
- grip
