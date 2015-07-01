Useful Unix Commands and Notes
==============================

_This is a compilation of commands that I have found particularly useful in a pinch. :+1:_

## Table of Contents

* [Networking](#networking)  
* [Benchmarking](#benchmarking)
* [find commands](#find-commands)  
* [curl commands](#curl-commands)  
* [vim commands](#vim-tips)
* [test commands](#test)
* [miscellanous commands](#misc-commands)  
* [file permissions](#file-permissions-chmod)  
* [SSH commands](#ssh-commands)

### Networking

* find what process is associated with a TCP port

```bash
$ /usr/sbin/lsof -i :8380
```
		
* See all TCP ports

```bash
$ /usr/sbin/lsof -Pnl +M -i4
```

* set system time

```
ntpdate 127.0.0.1 (replace with NTP server IP)
```

* ping Google DNS -- this is very useful for checking network reliability

```bash
ping -t 8.8.8.8
```

* [Digital Ocean: Mount an NFS drive on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-14-04) 

```bash
sudo mount 1.2.3.4:/volume1/myvolume /local/folder
```


### Benchmarking

* I/O performance benchmarks

```bash
hdparm -tT /dev/sda1
```
		
### `find` commands		

* find all files that were modified less that 2 days ago
 
```bash
find . -mtime -2
```

* find all files owned by root

```bash
find . -uid `id -u root`
```
	
* find all files 28 days old or newer

```bash
find . -name '*.log' -mtime -28
```
		
* find/replace with `sed`

```bash
find . -type f -exec sed -i 's/bad/good/g' {} \;
```
    
* find and remove files

```bash
find . -type f -exec rm {} \;
```
		
### `curl` commands

* Convert the .pfx to a PEM .cer -- this is a prereq to use a Java PFX cert in curl

```bash
openssl pkcs12 -in certificate.pfx -out certificate.cer -nodes
```

* run curl with the .cer

		curl -k https://{https_url} -E ~/certificate.cer:{cert_password}
	
* run curl with the http proxy and authentication

		curl -O some_url -x <host/>:<port/> -U <user/>:<pass/>

#### test
Some file `test` [flags](http://tldp.org/LDP/abs/html/fto.html). See also the [wikipedia](https://en.wikipedia.org/wiki/Test_(Unix)) article

* `-e` -- file exists
* `-f` -- file is a regular file
* `-d` -- file is a directory
* `!` -- negate
 
_Examples:_  

```bash
if test ! -s "$1"
 then
   echo $1 does not exist or is empty.
 fi
```



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
		
* list a directory sorted by size reversed
```bash
ls -lSr
```
* check a unique file size (better than `md5sum`)
```bash
sha1sum {file_name}
```
* human readable file sizes including summary of first level directories
```bash
du -h --max-depth=1 --all
```

* view configuration of services in `/etc/rc[0-9]/`.  The `chkconfig` can be used to administer all start up services.

```
sudo chkconfig --list
```


### vim tips

* for a case insensitive search use the `\c` escape sequence

		/\ccopyright

* `mark` locations

 	+ `ma` -- set the mark `a` at the current position
 	+ ```a`` -- jump to mark `a`
		
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


## SSH commands

### set up SSH keys

1. generate keys: `ssh-keygen -t rsa`
2. copy the public key: `ssh-copy-id user@host`

### SSH config

* turn off `GSSAPIAuthentication`
```bash
echo "GSSAPIAuthentication no" >> ~/.ssh/config
```

- <http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/>

-----

#### references

List of other useful Unix/Linux cheatsheets or tutorials:

* https://github.com/WilliamHackmore/linuxgems/blob/master/cheat_sheet.org.sh
* http://www.gregreda.com/2013/07/15/unix-commands-for-data-science/
* http://www.thegeekstuff.com/2012/08/lsof-command-examples/ (lsof examples)
* http://tldp.org/LDP/abs/html/ (Advanced Bash-Scripting)
* http://robertmuth.blogspot.com/2012/08/better-bash-scripting-in-15-minutes.html (Better Bash Scripting)
* https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
