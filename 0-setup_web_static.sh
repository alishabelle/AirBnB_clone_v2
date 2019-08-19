#!/usr/bin/env bash
# script sets up web server for deployment
apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
cat > /data/web_static/releases/test/index.html <<EOF
<html>
    <head>
    </head>
    <body>
        <p>simple content</p>
    </body>
</html>
EOF
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
cat > /etc/nginx/sites-available/default <<EOF
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html;

        location /hbnb_static {
                alias /data/web_static/current/;
        }
}
EOF
service nginx restart


