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

Git Workflow
============

* `git checkout -b dnorton-dev-2 origin/release-1.0.0` -- check out from a remote branch
* `git push -u origin dnorton-dev-2` -- push feature branch to remote repo
* `git pull origin dnorton-dev-2` -- pull feature branch
 
_add command to delete a remote feature branch here_


Read about the [Github Flow](http://scottchacon.com/2011/08/31/github-flow.html)


Git troubleshooting
===================

- to debug problems with an HTTP proxy set the environmental variable `GIT_CURL_VERBOSE=1`


### References

1. https://help.github.com/articles/adding-a-remote
2. http://git-scm.com/book
3. http://www.atlassian.com/git/tutorial
4. http://scottchacon.com/2011/08/31/github-flow.html
5. http://githubtraining.s3.amazonaws.com/github-git-training-slides.pdf (great training slides)
