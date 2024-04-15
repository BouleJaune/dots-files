# dots-files
My Archlinux dots file 

All custom system configurations should be explained here to ease the process of reinstalling the whole OS for my future me.

Some things are specific to this specific hardware, like nvidia conf or sensors kernel module.

## TODO:

Alacritty: improve padding + overall conf (theme)

Qtile: improve dmenu and status bar style, add focused border on full screen window

Add dots files that are not in .config

### Reason for the choice of some softwares

Why Qtile ? \
Cuz Python comfy

Why Alacritty ?\
Out of all the terminals I tried it's the only one with the least delay for redrawing screen after moving window, which is essential when you don't have any animations in your WM and it's tiling.

### Nvidia conf for suspend
To load all video memory in ram when suspending so that we don't have to refresh windows after sleep to not have a black screen :

```
/etc/modprobe.d/nvidia-power-management.conf
------------------------------------------------------------------
options nvidia NVreg_PreserveVideoMemoryAllocations=1 NVreg_TemporaryFilePath=/var/tmp
options nvidia-drm modeset=1
```

Then regenerate initramfs (maybe optional) ``mkinitcpio -P``\
Then ``systemctl enable nvidia-suspend.service && systemctl enable nvidia-hibernate.service``.\
And finally a reboot is probably a good idea.

### For fan control on b460 msi mag mortar : 

``nct6687`` install DKMS version of this module.\
``git clone https://github.com/Fred78290/nct6687d && cd nct6687d && make dkms/install``
Remember to remove the folder after this.

```
/etc/modprobe.d/sensors.conf
-------------------------
blacklist nct6683
```

### To have nested virt with intel cpu for KVM :
```
/etc/modprobe.d/kvm.conf
-----------------------
options kvm_intel nested=1
```

### Some modules to load

``/etc/modules-load.d/module.load`` :
```
i2c_dev
nct6687 #for the fan control again
btusb #to get usb
```

## Scripts: 
Folder is in the path, so all of them can be called as is. 

### record
``record screenNumber fps``\
Record screen at desired framerate, default to 25fps if no fps is specified. Output file is ``~/Vidéos/screen.mp4``\
Screen number is 1 or 2.

### sc

Screen capture the selection.\
Gets saved in ``~/Images/screen.png`` \
Copy to system clipboard the image.


### brightness

Takes a number ranging from 0 to 100 to set hardware luminosity through ddcutil and redshift.\
If the number is 0 then a low-blue light filter will be applied, if it's 100 it will be removed.

### tmux-sessionizer

Used through the shortcut ctrl+t in zsh.\
Opens up a fuzzyfinder menu to select a folder that will open OR attach a tmux session in that folder.

Slightly modified version of ThePrimeagen script: https://github.com/ThePrimeagen/.dotfiles/blob/master/bin/.local/scripts/tmux-sessionizer

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


### zsh :

oh my zsh + p10k
ctr + t open tmux-sessionizer
ll=ls -l
t=tmux a
vim=nvim
crkb="cd /home/xenio/Documents/qmk_firmware/keyboards/crkbd/keymaps/BouleJaune"
conf="cd /home/xenio/.config/"

### Discord :

Shortcuts : 
- ctrl + t : open a sorta fzf menu to go to channels
- esc : scroll to end of conv

### Rofi :
rofi + 
git clone --depth=1 https://github.com/adi1090x/rofi.git
Et suivre l'installation

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
- coolercontrol
- zathura-pdf-mupdf
- pavucontrol
- btop
- feh
- nix
- ranger

Python packages:
- grip (md viewer)

Language servers to install system wide : 
``'clangd', 'rust_analyzer', 'pylsp','tsserver', 'lua_ls', 'nil'``


Use : [https://wiki.archlinux.org/title/Language_Server_Protocol] to know which package needs to be installed. Except for nil which is not on the link.
