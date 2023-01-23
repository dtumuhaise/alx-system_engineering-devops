#!/usr/bin/env bash
# configure new web server and custom headers

# class for the custom header
class custom_http_response_header {
  package { 'nginx':
    ensure => installed,
  }
  file { '/etc/nginx/conf.d/custom_headers.conf':
    ensure  => file,
    content => "add_header X-Served-By ${::hostname};",
    notify  => Service['nginx'],
  }
  service { 'nginx':
    ensure => running,
    enable => true,
  }
}
