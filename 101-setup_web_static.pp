# Task 0 in puppet


exec {'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

exec {'ngnix_install':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
}

exec {'create_folder_1':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell,
}

exec {'create_folder_2':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => shell,
}

exec {'fake_index':
  command  => 'echo "Fake HTML file" | sudo tee /data/web_static/releases/test/index.html',
  provider => shell,
}

exec {'symbolic_link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
}

exec {'ownership':
  command  => 'chown  -R ubuntu:ubuntu /data/',
  provider => shell,
}

exec {'configure_content':
  command  => 'sed -ri "55i location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n" /etc/nginx/sites-available/default',
  provider => shell,
}

# Restart Nginx
exec { 'restart_service':
  command  => 'sudo service nginx start',
  provider => shell
}
