#! /usr/bin/env python3
""" Kettcar is a python module to parse git histories for conventional commit
messages. It can then generate SemVer versions based on the occurences of these
commit messages.
"""
import git

if __name__ == '__main__':
    commits = list(git.Repo("./").iter_commits())
    print("{} commits in this repository".format(len(commits)))

    print('Welcome to kettcar, nothing has been implemented yet')
