Useful git commands
-------------------

* view git configs

        git config -l

* set http proxy in git config

        git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080
        
from https://help.github.com/articles/adding-a-remote

* Set a new remote
        
        git remote add origin https://github.com/user/repo.git

* Verify new remote

        git remote -v


        # origin  https://github.com/user/repo.git (fetch)
        # origin  https://github.com/user/repo.git (push)

* `git diff --cached` - shows changes in index
* `git rm --cached` - remove file from staging but not working dir
