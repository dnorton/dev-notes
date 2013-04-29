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

		curl -k https://{https_url} -E ~/certificate.cer:{cert_password}
	
* run curl with the http proxy

		curl -O some_url -x <host/>:<port/>
	
* read a password

		read -es password  #reads the next line into $password and masks user input
	
* simple replacement for dos2unix (which is not standard)

		tr -d '\r' < dosfile > unixfile
	
	
* find what process is associated with a TCP port

		sudo /usr/sbin/lsof -i :8380
		
* See all TCP ports

		$ sudo /usr/sbin/lsof -Pnl +M -i4

* find a uid or gid for a user

		id -u username
		id -g username

* set http_proxy env variable

		http_proxy=http://username:password@hostname:port;
		export (or set on Windows) $http_proxy		
		
		
* list groups (this searches through naming directories as well as /etc/group)
		
		getent group|grep <group name/>
		
### rpm commands

* rpm query for any oracle package

 		rpm -qa|grep oracle

* list information about a package

		rpm -ql oracle-instantclient11.2-sqlplus-11.2.0.1.0-1



references
----------
List of other useful Unix/Linux cheatsheets:

* https://github.com/WilliamHackmore/linuxgems/blob/master/cheat_sheet.org.sh
