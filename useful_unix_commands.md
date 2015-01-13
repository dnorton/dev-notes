Useful Unix Commands and Notes
==============================

_This is a compilation of commands that I have found particularly useful in a pinch. :+1:_

## Table of Contents

* [networking](#networking)  
* [find commands](#find-commands)  
* [curl commands](#curl-commands)  
* [miscellanous commands](#misc-commands)  
* [file permissions](#file-permissions-chmod)  
* [SSH keys](#set-up-ssh-keys)

#### networking

* find what process is associated with a TCP port

```bash
$ /usr/sbin/lsof -i :8380
```
		
* See all TCP ports

```bash
$ /usr/sbin/lsof -Pnl +M -i4
```

* Replacement for `telnet`
	
		curl host:port
		
#### `find` commands		

* find all files that were modified less that 2 days ago
 
		find . -mtime -2

* find all files owned by root

		find . -uid `id -u root`
	
* find all files 28 days old or newer

		find . -name '*.log' -mtime -28
		
* find/replace with `sed`

		 find . -type f -exec sed -i 's/bad/good/g' {} \;
    
* find and remove files

		find . -type f -exec rm {} \;
		
#### `curl` commands

* Convert the .pfx to a PEM .cer -- this is a prereq to use a Java PFX cert in curl

		openssl pkcs12 -in certificate.pfx -out certificate.cer -nodes

* run curl with the .cer

		curl -k https://{https_url} -E ~/certificate.cer:{cert_password}
	
* run curl with the http proxy and authentication

		curl -O some_url -x <host/>:<port/> -U <user/>:<pass/>


#### misc commands		

* find/replace one liner in perl

		perl -p -i -e 's/oldstring/newstring/g' `find ./ -name *.html`

* traverse symlinks for a file and give the actual location
 
		readlink -f /usr/bin/java

	
* read a password

		read -es password  #reads the next line into $password and masks user input
	
* simple replacement for dos2unix (which is not standard)

		tr -d '\r' < dosfile > unixfile
		
* rename `*.bak` to `*`

		rename 's/\.bak$//' *.bak	
	
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

* system calls include child processes

		strace -f /bin/true		
		
* run a simple HTTP server using python (2.7+)

		python -m SimpleHTTPServer [port]
		
* cut the beginning of a value stored in a variable (see this [String manipulation in bash](http://tldp.org/LDP/abs/html/string-manipulation.html))

		TEST="remove.importantfile.txt"
		echo ${TEST#*.}
		
* cut the end of a value stored in a variable

		TEST="importantfile.txt.remove"
		echo ${TEST%.*}
	
* run a [junit test](https://github.com/junit-team/junit/wiki/Getting-started) from the command line 

		java -cp .:/usr/share/java/junit.jar org.junit.runner.JUnitCore [test class name]

* turn on debug with suspend=y (will wait for a remote debugger)

		DBUG="-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=10123"
		
* use [pygmentize](http://pygments.org/docs/cmdline/) to generate an HTML output of a diff file

		pygmentize -l diff -f html -O full -o diff.html diff.txt
		
* set proxy in npm

		npm config set https-proxy http://{user}:{password}@proxy.server:{port}
		
* pass env variables using sudo

		sudo -E bash -c 'echo $HTTP_PROXY'	
		
* capture command execution in a variable -- this example is useful for a date format string

		timestamp=$(date '+%Y%m%d%H%M')
		
* `bash` shell default to env value or use positional argument

		jboss_user=${jboss_user:-"$1"}
		
* tar up a directory but exclude logs

		tar cvfz mydir.tgz mydir --exclude mydir/logs
		

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

### set up SSH keys

1. generate keys: `ssh-keygen -t rsa`
2. copy the public key: `ssh-copy-id user@host`


-----

#### references

List of other useful Unix/Linux cheatsheets:

* https://github.com/WilliamHackmore/linuxgems/blob/master/cheat_sheet.org.sh
* http://www.gregreda.com/2013/07/15/unix-commands-for-data-science/
* http://www.thegeekstuff.com/2012/08/lsof-command-examples/ (lsof examples)
* http://tldp.org/LDP/abs/html/ (Advanced Bash-Scripting)
* http://robertmuth.blogspot.com/2012/08/better-bash-scripting-in-15-minutes.html (Better Bash Scripting)
* https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
