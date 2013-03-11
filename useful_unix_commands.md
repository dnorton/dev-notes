# useful unix commands
_This is a compilation of commands that I have found particularly useful in a pinch._

* traverse symlinks for a file and give the actual location
 
		readlink -f /usr/bin/java

* system calls include child processes

		sudo strace -f /bin/true
  
* find all files owned by root

		sudo find . -uid `id -u root`
		
* Find/Replace one liner in perl

		perl -p -i -e 's/oldstring/newstring/g' `find ./ -name *.html`
    
* Find and remove files

		find . -type f -exec rm {} \;
	
* Find what process is associated with a TCP port

		sudo /usr/sbin/lsof -i :8380
	

* Convert the .pfx to a PEM .cer -- this is useful when to use curl to test a Java PFX cert

		openssl pkcs12 -in certificate.pfx -out certificate.cer -nodes

* run curl with the .cer

		curl -k https://prodsvc.mib.com/01/S2SAdapter -E ~/certificate.cer:m1bQds
	
* run curl with the http proxy

		curl -O http://ftp.redhat.com/pub/redhat/linux/enterprise/6Workstation/en/os/SRPMS/repodata/repomd.xml -x <host/>:<port/>
	
* read a password

		read -es password  #reads the next line into $password and masks user input
	
* simple replacement for dos2unix (which is not standard)

		tr -d '\r' < dosfile > unixfile
	
	
* See all TCP ports

		$ sudo /usr/sbin/lsof -Pnl +M -i4

* find a uid or gid for a user

		id -u username
		id -g username

* set http_proxy env variable

		http_proxy=http://username:password@hostname:port;
		export (or set on Windows) $http_proxy		


references
----------
List of other useful Unix/Linux cheatsheets:

* https://github.com/WilliamHackmore/linuxgems/blob/master/cheat_sheet.org.sh
