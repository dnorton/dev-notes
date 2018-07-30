---
layout: post
title: Useful Git Commands
---

## Table of Contents

- [Git tricks](#git-tricks)
- [Git Commands](#git-commands)
    * [General git commands](#general-git-commands)
    * [Remote Commands](#remote-repo-commands)
    * [Local Repo Commands](#local-repo-commands)
- [Git Articles](#git-articles)
- [Git Workflow](#git-workflow) 
- [Github Cheatsheet](#github-cheatsheet)


## Git tricks

+ :clap: http://ohshitgit.com/
+ :bowtie: <http://www.alexkras.com/19-git-tips-for-everyday-use/>
+ :secret: [CIA's git tips & tricks](https://wikileaks.org/ciav7p1/cms/page_1179773.html)

### Git command line

* `git log --oneline --graph` -- great logging output
* `export GIT_CURL_VERBOSE=1;git clone ...` -- show the verbose output of the git curl

## Git usage

### General

* `git init` -- initialize a git repo in the current directory (you still need to add and commit the local files)
* `git config -l` -- view git configs
* `git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080` -- set http proxy in git config    
* `git branch -r --contains origin/my_release` -- find all remote branches that contain the commits in `my_release` branch
* `git diff-tree -r --root <SHA>` -- see a full diff-tree
* `git svn clone {svn_url}` -- clone an SVN repo as a git repository. _[more info](https://www.atlassian.com/git/tutorials/migrating-prepare)_

### Remote Repo Commands

* `git clone https://github.com/user/repo.git -o notorigin` -- sets the remote to "notorigin"
* `git clone -b branch_name https://github.com/user/repo.git` -- clone and checkout a specific remote branch
* `git remote add origin https://github.com/user/repo.git` -- set a new remote  
* `git remote set-url origin https://github.com/user/repo2.git` -- change the remote URL for `origin`
* `git remote update` -- update the local repo with remote tracking branches
* `git remote prune origin` -- remove stale tracking branches
* `git remote update` -- update branches from remote repos. Use this if you don't see you branch using `git branch -r`
* `git remote -v` -- verify new remote

```bash
        # origin  https://github.com/user/repo.git (fetch)
        # origin  https://github.com/user/repo.git (push)
```  

### Local Repo Commands

* `git branch -r` -- view available remote branches
* `git branch -vv` -- view the tracking branch
* `git checkout --track origin/serverfix` -- change the tracking branch
* `git diff --cached` -- shows changes in index  
* `git rm --cached` -- remove file from the index but not working dir
* `git clean -f -X -d` -- remove all unstaged files (great for cleaning up after a build)
* `git reset --hard HEAD` -- reset your local branch to the HEAD commit (see [Git Reset info](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset))
* `git checkout HEAD -- folder1/pom.xml` -- reset a single file to the HEAD commit
* `git show-ref` -- shows the `refs` for the repo (still figuring this out)
* `git filter-branch --prune-empty --subdirectory-filter lib master` -- split out a sub dir into a repository
* `git reset --soft HEAD~1` -- rollback a commit

### Git articles

+ [git reset (demystified)](https://git-scm.com/blog/2011/07/11/reset.html)
+ [The Golden rule of rebase](https://medium.freecodecamp.com/git-rebase-and-the-golden-rule-explained-70715eccc372#.2v8ra1b4f)

Git Workflow
============

Read about the [Github Flow](http://scottchacon.com/2011/08/31/github-flow.html)

* `git checkout -b dnorton-dev-2 origin/release-1.0.0` -- check out from a remote branch
* `git push -u origin dnorton-dev-2` -- push feature branch to remote repo
* `git pull origin dnorton-dev-2` -- pull feature branch
* `git push origin :dnorton-dev-2` -- delete the remote feature branch ([see the git-scm page](http://git-scm.com/book/en/Git-Branching-Remote-Branches#Deleting-Remote-Branches))

* Github help: [syncing a fork](https://help.github.com/articles/syncing-a-fork)

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
        
See [reference #7](http://stackoverflow.com/questions/2862590/how-to-replace-master-branch-in-git-entirely-from-another-branch) for more info.

- [github.com: how to undo almost anything with git](https://github.com/blog/2019-how-to-undo-almost-anything-with-git)

Github Cheatsheet
=================

+ Check out [Tim Green's Github Cheatsheet](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.md) :exclamation:
+ [Create git.io shortcuts URLs](https://github.com/blog/985-git-io-github-url-shortener)

### References

1. https://help.github.com/articles/adding-a-remote
2. http://git-scm.com/book
3. https://www.atlassian.com/git
4. http://scottchacon.com/2011/08/31/github-flow.html
5. http://githubtraining.s3.amazonaws.com/github-git-training-slides.pdf (great training slides)
6. http://gitolite.com/gcs.html#(1) (git concepts explained)
7. http://stackoverflow.com/questions/2862590/how-to-replace-master-branch-in-git-entirely-from-another-branch
8. https://github.com/tiimgreen/github-cheat-sheet :thumbsup:
