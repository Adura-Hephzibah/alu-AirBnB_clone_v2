#!/usr/bin/python3
"""
Module
"""
from fabric.api import put, run, local
from time import strftime
import os.path


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


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive_name = do_pack()
    if archive_name is None:
        return False
    status = do_deploy(archive_name)
    return status
