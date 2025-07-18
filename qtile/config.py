# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
import time
from subprocess import check_output

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, DropDown, ScratchPad
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "n", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "o", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "e", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Next window focus"),
    Key([mod], "g", lazy.window.toggle_floating(), desc="Next window focus"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "mod1"], "o", lazy.layout.swap_column_right(),
        desc="Move column to the right"),
    Key([mod, "mod1"], "n", lazy.layout.swap_column_left(),
        desc="Move column to the left"),
    Key([mod, "shift"], "n", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "o", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "e", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Key([mod, "control"], "n", lazy.layout.grow_left(),
    #     desc="Grow window to the left"),
    # Key([mod, "control"], "o", lazy.layout.grow_right(),
    #     desc="Grow window to the right"),
    # Key([mod, "control"], "e", lazy.layout.grow_down(),
    #     desc="Grow window down"),
    # Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.grow_main(), desc="Grow main window"),
    Key([mod, "control"], "i", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "e", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, "control"], "o", lazy.layout.shrink_main(), desc="Srhink window"),
    Key([mod], "b", lazy.hide_show_bar(), desc="Hides the bar"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # rofi run config
    Key([mod], 'v', lazy.run_extension(extension.DmenuRun(
        dmenu_prompt=">",
        dmenu_font="Andika-8",
        background="#240130",
        foreground="#00ff00",
        selected_background="#079822",
        selected_foreground="#fff",
        dmenu_lines=10,
    ))),
    Key([mod], 'm', lazy.next_screen(), desc='Next monitor'),
    Key([mod], 'r', lazy.spawn('rofi -show drun -dpi 200 -theme .config/rofi/launchers/type-7/style-2.rasi'), desc='rofi'),
    Key([mod], 'f', lazy.spawn('flameshot gui'), desc='clipping tool'),
    Key([mod], 'j', lazy.spawn('flameshot gui'), desc='clipping tool'),
    # topdown stuff
    Key([mod], 'z', lazy.group['scratchpad'].dropdown_toggle('draw')),
    Key([mod], 'x', lazy.group['scratchpad'].dropdown_toggle('term')),
]


def match_lorien_pid(c) -> None:
    time.sleep(0.1)
    try:
        pid = int(check_output(["pidof", 'lorien']))
        return c.get_pid() == pid
    # exception who cares
    except Exception:
        return False


groups = [
    Group("Main", spawn=["firefox"]),
    Group("Social", spawn=["vesktop"]),
    Group("Musique"),
    Group("Misc"),
    ScratchPad("scratchpad", [
        DropDown("draw", "lorien",
                 warp_pointer=True, on_focus_lost_hide=True,
                 match=Match(func=match_lorien_pid),
                 width=0.55, height=0.55, x=0.225, y=0.225),
        DropDown("term", "alacritty",
                 width=0.35, height=0.40, x=0.33, y=0.33),
    ]),
]

group_keys = ["l", "u", "y", "comma"]

for i in range(len(groups)):
    print(i)
    if i == 4:
        continue
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                group_keys[i],
                lazy.group[groups[i].name].toscreen(),
                desc="Switch to group {}".format(groups[i].name),
            ),
            Key([mod, "shift"], group_keys[i],
                lazy.window.togroup(groups[i].name),
                desc="move focused window to group {}".format(groups[i].name)),
        ]
    )

border_color_focus = "#8207b3"
border_color_normal = "#240130"

layouts = [
    layout.MonadThreeCol(
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=2,
        border_focus=border_color_focus,
        border_on_single=True,
        border_normal=border_color_normal),  # margin=5),
    layout.Columns(
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=2,
        border_focus=border_color_focus,
        border_on_single=True,
        border_normal=border_color_normal),  # margin=5),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(border_width=4,
    #                # border_focus=border_color_focus,
    #                # border_normal=border_color_normal,
    #                # margin=5,
    #                # align=1),  # main window to the right
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(fontsize=33,

    #                   section_fontsize=33,
    #                  panel_width=300),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
fontsize_4k = 20
fontsize_1440 = 17

screens = [

    Screen(
        bottom=bar.Bar(
            [
                widget.Spacer(length=1400),
                # widget.TextBox(text='Layout: ', fontsize=fontsize_4k),
                widget.CurrentLayout(fontsize=fontsize_4k),
                widget.Spacer(length=100),
                widget.GroupBox(center_aligned=True, fontsize=fontsize_4k),
                widget.Spacer(length=100),
                widget.WindowName(fontsize=fontsize_4k),
                widget.Spacer(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", fontsize=fontsize_4k),
            ],
            25,
            background='#410257',
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]
            # Borders are magenta
        ),

        #Static Wallpaper 

        wallpaper = '~/Images/wallpaper/neon-sunset-3840x2160_74456-mm-90.jpg',
        wallpaper_mode = 'fill'
    ),

    Screen(
        bottom=bar.Bar(
            [
                widget.Spacer(length=50),
                widget.GroupBox(center_aligned=True, fontsize=fontsize_1440),
                widget.Spacer(length=100),
                widget.TextBox(text='Current layout: ', fontsize=fontsize_1440),
                widget.CurrentLayout(fontsize=fontsize_1440),
                widget.Spacer(length=100),
                widget.Prompt(fontsize=fontsize_1440),
                widget.WindowName(fontsize=fontsize_1440),
                widget.Spacer(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.StatusNotifier(),
            ],
            26,
            background='#410257',
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]
            # Borders are magenta
        ),
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="dragon-term"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="Lorien"),  # Lorien
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
