---
layout: post
title: Useful Git Commands
---

Useful git commands
-------------------

* `git init` -- initialize a git repo in the current directory (you still need to add and commit the local files)
* `git config -l` -- view git configs
* `git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080` -- set http proxy in git config        
* `git clone https://github.com/user/repo.git -o notorigin` -- sets the remote to "notorigin"
* `git remote add origin https://github.com/user/repo.git` -- set a new remote  
* `git remote set-url origin https://github.com/user/repo2.git` -- change the remote URL for `origin`
* `git remote -v` -- verify new remote
* `git remote update` -- update branches from remote repos. Use this if you don't see you branch using `git branch -r`

```
        # origin  https://github.com/user/repo.git (fetch)
        # origin  https://github.com/user/repo.git (push)
```  

* `git branch -r` -- view available remote branches
* `git branch -vv` -- view the tracking branch
* `git checkout --track origin/serverfix` -- change the tracking branch
* `git diff --cached` -- shows changes in index  
* `git rm --cached` -- remove file from the index but not working dir
* `git clean -f -X -d` -- remove all unstaged files (great for cleaning up after a build)
* `git reset --hard HEAD` -- reset your local branch to the HEAD commit
* `git checkout HEAD -- folder1/pom.xml` -- reset a single file to the HEAD commit
* `git show-ref` -- shows the `refs` for the repo (still figuring this out)
* `git filter-branch --prune-empty --subdirectory-filter lib master` -- split out a sub dir into a repository

Git Workflow
============

Read about the [Github Flow](http://scottchacon.com/2011/08/31/github-flow.html)

* `git checkout -b dnorton-dev-2 origin/release-1.0.0` -- check out from a remote branch
* `git push -u origin dnorton-dev-2` -- push feature branch to remote repo
* `git pull origin dnorton-dev-2` -- pull feature branch
* `git push origin :dnorton-dev-2` -- delete the remote feature branch ([see the git-scm page](http://git-scm.com/book/en/Git-Branching-Remote-Branches#Deleting-Remote-Branches))

* Github help: [syncing a fork](https://help.github.com/articles/syncing-a-fork)


Git Misc Commands
=================

* `git diff-tree -r --root 40a450274b128348ec30d69abc51981ea7be20df` -- see a full diff-tree

Git Alias
=======
- Edit your ~/.gitconfig to add useful git aliases. see ([Effective pull requests and other good practices for teams using github](http://codeinthehole.com/writing/pull-requests-and-other-good-practices-for-teams-using-github/))

```
[alias]
    hist = log --color --pretty=format:\"%C(yellow)%h%C(reset) %s%C(bold red)%d%C(reset) 
    %C(green)%ad%C(reset) %C(blue)[%an]%C(reset)\" --relative-date --decorate
```


Git troubleshooting
===================

- to debug problems with an HTTP proxy set the environmental variable `GIT_CURL_VERBOSE=1`

### The `ours` merge technique to replace `master`

        git checkout seotweaks  
        git merge -s ours master  
        git checkout master  
        git merge seotweaks  
        
See reference #7 for more info.

### References

1. https://help.github.com/articles/adding-a-remote
2. http://git-scm.com/book
3. http://www.atlassian.com/git/tutorial
4. http://scottchacon.com/2011/08/31/github-flow.html
5. http://githubtraining.s3.amazonaws.com/github-git-training-slides.pdf (great training slides)
6. http://gitolite.com/gcs.html#(1) (git concepts explained)
7. http://stackoverflow.com/questions/2862590/how-to-replace-master-branch-in-git-entirely-from-another-branch
8. https://github.com/tiimgreen/github-cheat-sheet :thumbsup:
