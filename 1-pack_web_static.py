#!/usr/bin/python3
"""
Module
"""
from time import strftime
from fabric.api import local


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder of
    your AirBnB Clone repo
    """
    try:
        # All archives must be stored in the folder versions
        # (your function should create this folder if it doesn’t exist)
        local("mkdir -p versions")

        # The name of the archive created must be
        # web_static_<year><month><day><hour><minute><second>.tgz
        archive_name = "versions/web_static_{}.tgz".format(
            strftime("%Y%M%d%H%M%S"))

        # Create archive
        # All files in the folder web_static must be added to the final archive
        local("tar -cvzf {} web_static/".format(archive_name))

        # return the archive path
        return archive_name
    except Exception:
        return None
