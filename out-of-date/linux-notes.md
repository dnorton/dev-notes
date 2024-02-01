Ubuntu Tips
-----------

+ create a new Desktop icon

`sudo sublime /usr/share/applications/sublime.desktop`

+ install Java7

<verbatim>
sudo add-apt-repository ppa:webupd8team/java  
sudo apt-get update  
sudo apt-get install oracle-java7-installer  
</verbatim>

+ install deb package using `dpkg`

`sudo dpkg -i {file}.deb`

### Keyboard shortcults

+ `Alt` + `F2` -- pull up command bar
+ `Super` + `w` -- scale effect for desktop
+ `Super` + `s` -- zoom out and show all workspaces
+ `Ctl` + `Shift` + `Alt` + `[left/right]` -- move window to left or right workspace

### Ubuntu References

* [Keyboard Shortcuts](https://help.ubuntu.com/community/KeyboardShortcuts)
* http://www.ubuntugeek.com/how-to-install-oracle-java-7-in-ubuntu-12-04.html

RedHat Tips
-----------

### rpm commands

* rpm query for any oracle package

 		rpm -qa|grep oracle

* list information about a package

		rpm -ql oracle-instantclient11.2-sqlplus-11.2.0.1.0-1
		

### Joining Microsoft AD

- https://technet.microsoft.com/en-us/library/2008.12.linux.aspx
