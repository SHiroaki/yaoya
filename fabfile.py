#-*- coding: utf-8 -*-
from fabric.api import local

def hello(name="world"):
    print("Hello %s" % name)

def commit(message="default commit"):
    local("git add -p && git commit -m \"%s\"" % message)

def push():
    local("git push origin master")

