# Mac Workspace

This is my Mac woskspace setup.

## Terminal Setup

- [ohnmyzsh](https://ohmyz.sh/)
- [neovim](./neovim.md)
- [homebrew](https://brew.sh/)
- [fzf](https://github.com/junegunn/fzf)

Configure `zsh`:

- install `omz`

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Configure `fzf`:

```bash
brew install fzf

# To install useful key bindings and fuzzy completion:
$(brew --prefix)/opt/fzf/install
```
