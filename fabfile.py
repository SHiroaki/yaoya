#-*- coding: utf-8 -*-

import subprocess
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ["ec2-52-192-156-109.ap-northeast-1.compute.amazonaws.com"]
env.user = "gituser"
env.key_filename = "~/.ssh/id_git_rsa"
env.local_src_path = "/home/hiroaki/working"

def hello(name="world"):
    print("Hello %s" % name)

def get_commit_id():
    """
    ~/woking/ディレクトリのmaster branchのcommit idを取得する
    """
    with lcd(env.local_src_path): # lcdされないsubprocessだと無効?
        commit_log = local("git log --graph --oneline", capture=True)
    print(commit_log)
    print("--------------------------------------")
    commit_id = input("Commit ID >>")
    if not confirm("Do you want to rallback to Commit ID : %s ?" % commit_id):
        abort("Aborting at rollback request.")
    return commit_id

def test():
    """
    confirmはプロンプト上にY/nの選択肢を表示する
    capture=Trueにするとコマンドの結果を見れる. .failed or return_codeで
    """

    with settings(warn_only=True):
        result = local("nosetests", capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting ad user request.")

def commit(message="default commit"):
    local("git add -A && git commit -m \"%s\"" % message)

def push():
    local("git push origin master")

def pre_deploy():
    with lcd(env.local_src_path):
        #test()
        print(env.local_src_path)
        commit()
        push()

def deploy():
    code_dir = "~/working/"
    with cd(code_dir): # デプロイ先ディレクトリに移動して
        run("git pull ~/repos/working.git master") # リモートで実行する

def rollback():
    """
    working ディレクトリでgit log --graph --onelineしてcommit idを取得すること
    最後のcommitが最初に表示される
    """
    commit_id = get_commit_id()
    with lcd(env.local_src_path):
        local("git revert %s" % commit_id)
        push()
