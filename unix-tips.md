Useful Unix Commands and Notes
==============================

_This is a compilation of commands that I have found particularly useful in a pinch. :+1:_

## Table of Contents

* [Networking](#networking)
	* [SSL commands](#ssl) 	
	* [TCP commands](#tcp-commands) 	
	* [curl commands](#curl-commands)  
	* [SSH commands](#ssh-commands)
* [System](#system)
	* [Benchmarking](#benchmarking)
* [Every Day Commands](#every-day-commands)
	* [find commands](#find-commands)
	* [rsync commands](#rsync)
	* [test commands](#test)
	* [miscellanous commands](#misc-commands)  
	* [file permissions](#file-permissions-chmod)  
* [References](#references)
	* [Reading List](#reading-list) 	

## Networking

### SSL

- [ ] read http://www.planetlarg.net/support-cookbook/ssl-secure-sockets-layer

* view a `.pfx` file using `keytool` (read [what is PKCS12](http://stackoverflow.com/questions/6157550/what-is-the-difference-between-a-pkcs12-keystore-and-a-pkcs11-keystore))

```bash
keytool -list -keystore file.pfx -storetype PKCS12
```

* Convert the .pfx to a PEM .cer -- this is a prereq to use a Java PFX cert in curl

```bash
openssl pkcs12 -in certificate.pfx -out certificate.cer -nodes
```

### TCP commands

* find what process is associated with a TCP port

```bash
$ /usr/sbin/lsof -i :8380
```
		
* See all TCP ports

```bash
$ /usr/sbin/lsof -Pnl +M -i4
```

* ping Google DNS -- this is very useful for checking network reliability

```bash
ping -t 8.8.8.8
```

### `curl` commands

* run curl with the .cer

```bash
curl -k https://{https_url} -E ~/certificate.cer:{cert_password}
```
	
* run curl with the http proxy and authentication

```bash
curl -O some_url -x <host/>:<port/> -U <user/>:<pass/>
```
		
## SSH commands

### set up SSH keys

1. generate keys: `ssh-keygen -t rsa`
2. copy the public key: `ssh-copy-id user@host`

### SSH config

* turn off `GSSAPIAuthentication`

```bash
echo "GSSAPIAuthentication no" >> ~/.ssh/config
```

* turn off `StrictHostKeyChecking` in ssh

```bash
ssh -o StrictHostKeyChecking=no <user>@<host> -i <priv_key_loc> 
```


## System

* [Digital Ocean: Mount an NFS drive on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-14-04) 

```bash
sudo mount 1.2.3.4:/volume1/myvolume /local/folder
```

* set system time

```
ntpdate 127.0.0.1 (replace with NTP server IP)
```

### Benchmarking

* I/O performance benchmarks

```bash
hdparm -tT /dev/sda1
```

## Every Day Commands
		
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

### rsync

- [ ] read: http://www.thegeekstuff.com/2010/09/rsync-command-examples/

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

```bash
perl -p -i -e 's/oldstring/newstring/g' `find ./ -name *.html`
```

* traverse symlinks for a file and give the actual location
 
```bash
readlink -f /usr/bin/java
```

* read a password

```bash
read -es password  #reads the next line into $password and masks user input
```
	
* simple replacement for dos2unix (which is not standard)

```bash
tr -d '\r' < dosfile > unixfile
```
		
* rename `*.bak` to `*`

```bash
rename 's/\.bak$//' *.bak
```
	
* find a uid or gid for a user

```bash
id -u username
id -g username
```

* set http_proxy env variable

```bash
http_proxy=http://username:password@hostname:port;
export (or set on Windows) $http_proxy
```
	
* list groups (this searches through naming directories as well as /etc/group)

```bash
getent group|grep <group name/>
```

* use `getent` to retrieve a service user name

```bash
getent passwd|grep maven|awk -F\: '{print $1}'
```

* system calls include child processes

```bash
strace -f /bin/true		
```

* run a simple HTTP server using python (2.7+)

```bash
python -m SimpleHTTPServer [port]
```
	
* cut the beginning of a value stored in a variable (see this [String manipulation in bash](http://tldp.org/LDP/abs/html/string-manipulation.html))

```bash
TEST="remove.importantfile.txt"
echo ${TEST#*.}
```

* cut the end of a value stored in a variable

```bash
TEST="importantfile.txt.remove"
echo ${TEST%.*}
```
	
* use [pygmentize](http://pygments.org/docs/cmdline/) to generate an HTML output of a diff file

```bash
pygmentize -l diff -f html -O full -o diff.html diff.txt
```
		
* pass env variables using sudo

```bash
sudo -E bash -c 'echo $HTTP_PROXY'
```
		
* capture command execution in a variable -- this example is useful for a date format string

```bash
timestamp=$(date '+%Y%m%d%H%M')
```
		
* `bash` shell default to env value or use positional argument

```bash
jboss_user=${jboss_user:-"$1"}
```
		
* tar up a directory but exclude logs

```bash
tar cvfz mydir.tgz mydir --exclude mydir/logs
```
		
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

* generate a random 15 character password
```bash
head -c 500 /dev/urandom | tr -dc a-zA-Z0-9\.\^\*\? | head -c 15; echo
```

		
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

### References

#### Reading List

- [ ] https://github.com/jlevy/the-art-of-command-line

**List of other useful Unix/Linux cheatsheets or tutorials:**

* https://github.com/alebcay/awesome-shell :boom:
* https://github.com/WilliamHackmore/linuxgems/blob/master/cheat_sheet.org.sh
* http://www.gregreda.com/2013/07/15/unix-commands-for-data-science/
* http://www.thegeekstuff.com/2012/08/lsof-command-examples/ (lsof examples)
* http://tldp.org/LDP/abs/html/ (Advanced Bash-Scripting)
* http://robertmuth.blogspot.com/2012/08/better-bash-scripting-in-15-minutes.html (Better Bash Scripting)
* https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
* http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file
