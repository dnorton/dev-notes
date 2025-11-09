# My workspace setup

- [tmux](./tmux.md)
- [neovim](neovim.md)
- [starship](https://starship.rs/) - cross-shell prompt
- [fzf](https://github.com/junegunn/fzf) - command-line fuzzy finder
- [alacritty](https://alacritty.org)
- [ghostty](https://ghostty.org)

### Alacrity links

- <https://alacritty.org/config-alacritty-bindings.html> - key bindings for Alacritty

### Ghostty links

- [config](https://ghostty.org/docs/config#reloading-the-configuration)

Ghostty sends the term `xterm-ghostty` to the remote server. This can be changed to `xterm-256color` by setting the `TERM` environment variable.

```bash
[ec2-user@ip-10-0-5-226 ~]$ echo $TERM
xterm-ghostty
[ec2-user@ip-10-0-5-226 ~]$ export TERM=xterm-256color
[ec2-user@ip-10-0-5-226 ~]$ ls
scripts
[ec2-user@ip-10-0-5-226 ~]$
```
