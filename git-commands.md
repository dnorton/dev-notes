Useful git commands
-------------------

* `git init` -- initialize a git repo in the current directory (you still need to add and commit the local files)
* `git config -l` -- view git configs
* `git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080` -- set http proxy in git config        
* `git remote add origin https://github.com/user/repo.git` -- set a new remote        
* `git remote -v` -- verify new remote

```
        # origin  https://github.com/user/repo.git (fetch)
        # origin  https://github.com/user/repo.git (push)
```  

* `git diff --cached` -- shows changes in index  
* `git rm --cached` -- remove file from the index but not working dir


Git troubleshooting
===================

- to debug problems with an HTTP proxy set the environmental variable `GIT_CURL_VERBOSE=1`


### References

1. https://help.github.com/articles/adding-a-remote
2. http://git-scm.com/book
3. http://www.atlassian.com/git/tutorial
