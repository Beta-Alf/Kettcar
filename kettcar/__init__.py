#! /usr/bin/env python3
""" Kettcar is a python module to parse git histories for conventional commit
messages. It can then generate SemVer versions based on the occurences of these
commit messages.
"""
import git
import argparse
import re


def parse_commit_message(message):
    minor_re = re.compile("\Afeat:")
    if minor_re.match(message):
        print("matched a feature")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path of the repo to be analyzed")
    args = parser.parse_args()
    commits = list(git.Repo(args.path).iter_commits())
    for c in commits[::-1]:
        parse_commit_message(c.message)

    print("{} commits in this repository".format(len(commits)))

    print('Welcome to kettcar, nothing has been implemented yet')
