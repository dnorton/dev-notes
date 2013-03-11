# useful unix commands
_This is a compilation of commands that I have found particularly useful in a pinch._

* traverse symlinks for a file and give the actual location
 
		readlink -f /usr/bin/java

* system calls include child processes

		sudo strace -f /bin/true
  
* find all files owned by root

		sudo find . -uid `id -u root`


references
----------
List of other useful Unix/Linux cheatsheets:

* https://github.com/WilliamHackmore/linuxgems/blob/master/cheat_sheet.org.sh
