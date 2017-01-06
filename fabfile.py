#-*- coding: utf-8 -*-
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def hello(name="world"):
    print("Hello %s" % name)

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
    local("git add -p && git commit -m \"%s\"" % message)

def push():
    local("git push origin master")

def prepare_deploy():
    test()
    commit()
    push()
