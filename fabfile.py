#-*- coding: utf-8 -*-
from fabric.api import local

def hello(name="world"):
    print("Hello %s" % name)

