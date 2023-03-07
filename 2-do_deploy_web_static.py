#!/usr/bin/python3
"""
Module
"""
from fabric.api import put, run
import os.path


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if os.path.exists(archive_path) is False:
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        file = archive_path.split("/")[-1]
        file_name = file.split(".")[0]
        folder = "/data/web_static/releases/{}/".format(file_name)
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))

        # Delete the archive from the web server
        run("rm -r /tmp/{}".format(file))

        run("mv {}web_static/* {}".format(folder, folder))
        run("rm -rf {}web_static".format(folder))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current on
        # the web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        run("ln -s {} /data/web_static/current".format(folder))
        return True
    except Exception:
        return False
