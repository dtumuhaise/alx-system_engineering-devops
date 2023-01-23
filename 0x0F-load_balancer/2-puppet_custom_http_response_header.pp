#!/usr/bin/env bash
# configure new web server and custom headers

sudo apt-get update
sudo apt-get install nginx -y
sudo apt-get install puppet -y
sudo puppet module install puppetlabs-nginx
sudo apply <<EOF
class { 'nginx': }

nginx::resource::server { '70942-web-02':
  listen      => [ '80' ],
  server_name => '70942-web-02',
  access_log  => '/var/log/nginx/access.log',
  error_log   => '/var/log/nginx/error.log',
  root        => '/var/www/html',
  location    => {
    '/' => {
      'add_header' => [ 'X-Served-By' ],
    }
  },
}
EOF

sudo service nginx restart
