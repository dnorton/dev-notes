# Learning NeoVim

- Info: [NeoVim](https://neovim.io/) is a fork of [Vim](https://www.vim.org/)
- Setup Video: [Zero to IDE](https://www.youtube.com/watch?v=N93cTbtLCIM)

see [vim-tips](../editors/vim-tips.md) for more on using vim

## Mason

[Mason](https://github.com/williamboman/mason-lspconfig.nvim) - is a plugin that helps you install and configure LSP servers.

To use, run `:Mason` and select the language server you want to install.  
To see help `:help mason.nvim`

## Custom Configs

- [Abazzi config](https://github.com/Abazzi/nvim/tree/main/lua/core)

## LazyVim

[LazyVim](https://lazyvim.org/) is a plugin that makes it easy to install and manage other plugins.

### KeyMappings

Navigate around the buffers using the following key mappings:

- `Ctrl + h` - Move to the left buffer
- `Ctrl + l` - Move to the right buffer
- `Ctrl + j` - Move to the bottom buffer
- `Ctrl + k` - Move to the top buffer

Additional buffer commands

- `[ + b` - Move to the left buffer
- `] + b` - Move to the right buffer

_Leader key commands in Lazy_

- `<space> + f + b` - Open the file explorer
- `<space> + s + k` - Search key mappings

Buffers

- `:bd` - Delete the current buffer

## Kickstarter

[Kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim)

This is a very small neovim configuration that let's you learn
as you go. You can always go back to LazyVim if you back up properly.

Some tips and tricks for out of the box Kickstarter:
(basic LSP functions)

- `:Telescope keymaps` - shows the keymaps for the Telescope plugin
- `gd` - go to definition
- `gr` - look for references
- `<Space>+d+s` - shows symbols in current file
- `<Space>s+f` - search files

## Plugins

- [go.nvim](https://github.com/ray-x/go.nvim)
- [copilot.nvim](https://github.com/github/copilot.vim)
- [clipboard-image.nvim](https://github.com/dfendr/clipboard-image.nvim)

Clipboard Image uses `:PasteImg` to paste an image from the clipboard.

## Lua

Lua is the scripting language built into `neovim`

```
  you can explore or search through `:help lua-guide`
  - https://neovim.io/doc/user/lua-guide.html
```

## Snacks

<https://github.com/folke/snacks.nvim>
