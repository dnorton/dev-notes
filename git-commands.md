Useful git commands
-------------------

* `git config -l` -- view git configs
* `git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080` -- set http proxy in git config        
* `git remote add origin https://github.com/user/repo.git` -- set a new remote        
* `git remote -v` -- verify new remote

        # origin  https://github.com/user/repo.git (fetch)
        # origin  https://github.com/user/repo.git (push)
        
* `git diff --cached` -- shows changes in index
* `git rm --cached` -- remove file from the index but not working dir

### References

1. https://help.github.com/articles/adding-a-remote
