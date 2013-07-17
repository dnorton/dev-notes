# useful unix commands
_This is a compilation of commands that I have found particularly useful in a pinch._

* traverse symlinks for a file and give the actual location
 
		readlink -f /usr/bin/java

* system calls include child processes

		strace -f /bin/true
  
* find all files owned by root

		find . -uid `id -u root`
	
* find all files 28 days old or newer

		find . -name '*.log' -mtime -28
		
* find/replace one liner in perl

		perl -p -i -e 's/oldstring/newstring/g' `find ./ -name *.html`
		
* find/replace with `sed`

		 find . -type f -exec sed -i 's/bad/good/g' {} \;
    
* find and remove files

		find . -type f -exec rm {} \;

* Convert the .pfx to a PEM .cer -- this is a prereq to use a Java PFX cert in curl

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

		/usr/sbin/lsof -i :8380
		
* See all TCP ports

		/usr/sbin/lsof -Pnl +M -i4

* find a uid or gid for a user

		id -u username
		id -g username

* set http_proxy env variable

		http_proxy=http://username:password@hostname:port;
		export (or set on Windows) $http_proxy		
		
		
* list groups (this searches through naming directories as well as /etc/group)
		
		getent group|grep <group name/>

* use `getent` to retrieve a service user name

		getent passwd|grep maven|awk -F\: '{print $1}'
		
* turn off `StrictHostKeyChecking` in ssh

		ssh -o StrictHostKeyChecking=no <user>@<host> -i <priv_key_loc> 
		
* run a simple HTTP server using python

		python -m SimpleHTTPServer [port]
		
* cut the beginning of a value stored in a variable (see this [String manipulation in bash](http://tldp.org/LDP/abs/html/string-manipulation.html))

		TEST="remove.importantfile.txt"
		echo ${TEST#*.}
		
* cut the end of a value stored in a variable

		TEST="importantfile.txt.remove"
		echo ${TEST%.*}
	
		
### rpm commands

* rpm query for any oracle package

 		rpm -qa|grep oracle

* list information about a package

		rpm -ql oracle-instantclient11.2-sqlplus-11.2.0.1.0-1
		

### vim tips

* for a case insensitive search use the `\c` escape sequence

		/\ccopyright
		
### file permissions (`chmod`)


|  #  | Permission        | rwx |
| --- | ----------------- | --- |
| 7   | full              | 111 |
| 6   | read and write    | 110 |
| 5   | read and execute  | 101 |
| 4   | read only         | 100 |
| 3   | write and execute | 011 |
| 2   | write only        | 010 |
| 1   | execute only      | 001 |
| 0   | none              | 000 |



-----

#### references

List of other useful Unix/Linux cheatsheets:

* https://github.com/WilliamHackmore/linuxgems/blob/master/cheat_sheet.org.sh
* http://www.gregreda.com/2013/07/15/unix-commands-for-data-science/
