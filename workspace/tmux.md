# tmux notes

## Info

- [Beginners guide to tmux (redhat)](https://www.redhat.com/sysadmin/introduction-tmux-linux)
- [tmux cheatsheet](https://tmuxcheatsheet.com/)

## Getting Started

Install on MacOS:

`brew install tmux`

## Commands

- `tmux new -s session1` - create a new tmux session
- `tmux ls` - list sessions
- `tmux a - t session1` - attach to existing session

_Commands inside tmux:_

These commands use `<Ctr+b>`. I'll refer to it as `<Leader>`

- `tmux` - start tmux session
- `<Leader> d` - detach (or whatever Leader you set)
- `<Leader> ?` - help (dismiss with `q`)
- `<Leader> + :resize-pane -` + `D,U,L, or R` -- (e.g., `:resize-pane -R 10` to expand right by 10)
- `<Leader> + <option>+(up,down,left,right)` - also resize

## Configuration

Create the file `~/.tmux.conf`

Set the default shell

```conf
#set the default shell
set -g default-shell /bin/zsh
```

From the `man tmux` info:

```
-f file       Specify an alternative configuration file.  By default, tmux loads the system configuration file from /opt/homebrew/etc/tmux.conf, if present, then looks for a user configuration file at
                   ~/.tmux.conf, $XDG_CONFIG_HOME/tmux/tmux.conf or ~/.config/tmux/tmux.conf.
```

## TPM

[dreams of code tmux config](https://github.com/dreamsofcode-io/tmux)
[catppuchin plugin](https://github.com/catppuccin/tmux)

