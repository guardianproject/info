---
id: 11959
title: A tag-team git workflow that incorporates auditing
date: 2013-11-21T14:03:22-04:00
author: Hans-Christoph Steiner
layout: post
guid: https://guardianproject.info/?p=11959
permalink: /2013/11/21/a-tag-team-git-workflow-that-incorporates-auditing/
categories:
  - HowTo
tags:
  - git
  - workflow
---
Git is as wonderful as it is terrible, it is immensly flexible but also far from intuitive. So to make our lives easier, we try to use git as it was originally intended, as a toolkit for building workflows.

<div id="attachment_11990" style="width: 310px" class="wp-caption alignright">
  <a href="http://git-scm.com/book/en/Distributed-Git-Distributed-Workflows#Integration-Manager-Workflow"><img aria-describedby="caption-attachment-11990" src="https://guardianproject.info/wp-content/uploads/2013/11/integration_manager_workflow-300x121.png" alt="Integration-Manager Workflow" width="300" height="121" class="size-medium wp-image-11990" srcset="https://guardianproject.info/wp-content/uploads/2013/11/integration_manager_workflow-300x121.png 300w, https://guardianproject.info/wp-content/uploads/2013/11/integration_manager_workflow.png 500w" sizes="(max-width: 300px) 100vw, 300px" /></a>
  
  <p id="caption-attachment-11990" class="wp-caption-text">
    Integration-Manager Workflow
  </p>
</div>We use a simple version of the “

<a href="http://git-scm.com/book/en/Distributed-Git-Distributed-Workflows" target="_blank">Integration-Manager Workflow</a>“. One key difference is that we often have multiple contributors acting as the integration manager. This means that there is always someone else besides the original author reviewing each commit. For example: I make a commit and push it to my public developer’s repo. I ask Abel to review my commit, and if he agrees with it, he then pushes it to the official public “_upstream_” repo (aka “blessed repository”). And since git will tell us if a remote repo is different than our local repo, this process makes it harder for an attacker to slip a commit into our remote repo without us noticing.

The key to this workflow is that all contributors must fork from the same git repo, and mark that one as the one _upstream_ repo. We often end up <a href="http://git-scm.com/book/en/Git-Branching-Rebasing" target="_blank">rebasing</a> things to make sure each commit is based on the most up-to-date code. It also makes for a clean, readable history. That means each contributor’s public repo will be rebased from time to time, so you cannot rely on those repos as something to base your own work off of.

At the very least, a contributor’s local repo should be set up to talk to two remote repos: the contributor’s own public repo and the _upstream_ repo. I’ll use github as an example of how to get started in this workflow. Say you want to contribute to https://github.com/guardianproject/keysync, start by making a fork via the github.com<img src="https://guardianproject.info/wp-content/uploads/2013/11/fork.png" alt="fork" width="65" height="19" /> button. Once that is setup, its time to clone it and configure the rest. I’m **eighthave** on github, so this example will use my public repo. I work with Abel Luck on KeySync, so we’ll add his repo as another contributor repo.

```
git clone https://github.com/eighthave/keysync
cd keysync
git remote add upstream https://github.com/guardianproject/keysync
git fetch upstream
git remote add abeluck https://github.com/abeluck/keysync
git fetch abeluck
```

Now I can see all of the remotes in my local git repo, and work with them as branches: 

```console
$ git remote  -v
abeluck https://github.com/abeluck/keysync (fetch)
abeluck https://github.com/abeluck/keysync (push)
origin  https://github.com/eighthave/keysync (fetch)
origin  https://github.com/eighthave/keysync (push)
upstream        https://github.com/guardianproject/keysync (fetch)
upstream        https://github.com/guardianproject/keysync (push)
$ git branch -va
* master                  1536fcf parse version number from setuptools
  remotes/abeluck/master  1536fcf parse version number from setuptools
  remotes/origin/HEAD     -> origin/master
  remotes/origin/master   1536fcf parse version number from setuptools
  remotes/upstream/master 1536fcf parse version number from setuptools
```

Now I do some work, and commit it to my local repo, and want to push them for Abel to review. In the meantime Abel has pushed some commits for me to review into his remote repo `abeluck`. So I need to fetch his new commits, then rebase my new local commits on top of of his new commits. When its all ready, I push it to my remote repo `origin`.

```
git checkout master
git fetch abeluck
(review the commits...)
git rebase abeluck/master
git push origin master
```

Now I’ve reviewed Abel’s new commits and incorporated them into my public repo. Abel is ready to review my new commits, which are rebased on top of his. If he agrees with them, he’ll push them to the official “blessed” repo `upstream`. Then his local repo will be in sync with the latest _upstream_.

```
git checkout master
git fetch eighthave
git merge eighthave/master
(review the commits...)
git push upstream master
```


**Review The Commits**

You can also review the commits before rebasing or merging them into the local master. This is done by switching to the remote branch, which is kind of like a local branch, but not entirely. It works for checking out and viewing just fine though:

```
git checkout eighthave/master
(review the commits...)
git checkout master
```

**Undoing A Bad Rebase**

Git doesn’t provide any undo, and it also will let you delete things, not a good situation for learning this stuff. Luckily it does give you the tools for making something like an undo function. I use a tag for this, and I always use the same name for that tag: `pre-rebase`. Before starting anything that involves rebasing, I first do:

```
git checkout master
git tag pre-rebase
```

Then after the rebase is successfully deleted, I remove that tag:

```
git tag -d pre-rebase
```

**Switching Your Master When Things Have Diverged**

It is often the case that in the process of merging and rebasing, the developers’ repos will be in separate branches of the original tree. Once the “integration manager” person has pulled in all the commits, rebased and merged everything, and pushed the approved commits to the upstream repo, the other developers will likely need to reset their repos to resync with the upstream:

```
git fetch upstream
git checkout upstream/master
git branch -D master
git branch master
git checkout master
git push -f origin master
```

So `git branch -D master` does indeed mean force-delete your master branch. That is required before setting your master branch to a new branch. If you want, you can keep that old branch around by doing `git branch myfeaturedevbranch` before doing `git branch -D master`.

**Keeping All The History**

One addition to this process is for each contributor to mark their own tree with a labeled branch before rebasing, and then pushing those branches to the contributor’s public repo. This will then provide a complete history of the process, if that is desired. For example: I push some commits to my public repo, then Abel rebases my commits onto some of his work and pushes to the _upstream_. In this case, the history in my public repo will be different than what is in the _upstream_ repo as well as Abel’s public repo.