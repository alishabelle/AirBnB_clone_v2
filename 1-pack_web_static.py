#!/usr/bin/python3
""" fabric script generates .tgz file """

from fabric.api import *
import datetime

def do_pack():
    """ final archive """
    local("mkdir -p versions")
    date = datetime.datetime.strftime("%Y %b %d %H %M %S")
    create = ('versions/web_static_' + 'date' + '.tgz')
    gen = fabric.api.local("tar -cvzf {} web_static".format(create))

    if gen:
        return None
    else:
        return create
