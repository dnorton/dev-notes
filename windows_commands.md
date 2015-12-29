Windows Commands
----------------

_This is just a collection of useful Windows commands_

* `where python` -- like the Unix `which python`, locates the installed path to `python`
* clear `.bat` file app association -- http://superuser.com/questions/53948/how-do-i-restore-bat-files-as-executables
* `rmdir /S dir_name` -- remove a non-empty directory
* `ctrl + shift + esc` -- open task manager
* [if else block with exist](https://gist.github.com/dnorton/eeed81c93dda9a82163a) -- a gist to check for directory existence in batch script
* `mklink /D nameDir sourceDir` -- create a symlink directory named `nameDir` that points to `sourceDir`
* `rd nameDir` -- remove `nameDir` directory symlink. _must be done first if symlink already exists in mklink above_

## Windows Utilities

- [Microsoft File Checksum Integrity Verifier](http://www.microsoft.com/en-us/download/details.aspx?id=11533) -- installs `fciv`
  * `fciv {path_to_file} -sha1` -- generate the SHA1 value of a file   
