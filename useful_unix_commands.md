# useful unix commands

* traverse symlinks for a file and give the actual location
 
		readlink -f /usr/bin/java

* system calls include child processes

		sudo strace -f /bin/true
  
* find all files owned by root

		sudo find . -uid `id -u root`
