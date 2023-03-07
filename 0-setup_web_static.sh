#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

LOCATION_VAR="location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n"

# Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# create some folders if don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "Fake HTML file" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
# If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group. This should be recursive
chown  -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -ri "s/location\s/$LOCATION_VAR/" /etc/nginx/sites-available/default

# restart Nginx after updating the configuration
sudo service nginx start