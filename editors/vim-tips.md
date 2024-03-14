VIM Tips and Tricks
===================

- [vim cheatsheet](https://vim.rtorr.com/)

## Keyboard shortcuts

* [gist - keyboard shortcuts](https://gist.github.com/awidegreen/3854277)
* [vim motion diagrams](https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/moving-blazingly-fast-with-the-core-vim-motions/)
* in Neovim, type `:Tutor` for some common VIM motions

### Bookmarks

* `mark`[*](http://vim.wikia.com/wiki/Using_marks) locations

 	+ `ma` -- set the mark `a` at the current position
 	+ `` `a`` -- jump to mark `a`
	+ `:marks` -- show bookmarks

* search

	+ `f+<char>` - jump to a character on the line
    	+ `;` - after using `f`, this will jump to next match, `,` go back
  	+ `t+<char>` - jump to character before
  	+ `F+<char>` - jump backwards to character
	
* `scroll`[*](http://vimdoc.sourceforge.net/htmldoc/scroll.html)

	+ `zt` -- scroll current line to top of screen
	+ `z.` -- scroll current line to middle of screen
	+ `zb` -- scroll current line to bottom of screen

* `goto`

	+ `G` - jump to bottom of file
	+ `gg` - jump to top of file 

### `.vimrc` files

- http://vim.wikia.com/wiki/Example_vimrc
- http://spf13.com/post/perfect-vimrc-vim-config-file
- [view vimrc file](http://vim.wikia.com/wiki/Open_vimrc_file)

### vim tricks

* for a case insensitive search use the `\c` escape sequence

		/\ccopyright

