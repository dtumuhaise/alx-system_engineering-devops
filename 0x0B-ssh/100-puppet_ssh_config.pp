#!/usr/bin/env bash
# client config file using puppet

ssh_authorized_key { 'school_key':
  user => 'ubuntu',
  type => 'ssh-rsa',
  key  => file('~/.ssh/school'),
}

ssh_config { 'PasswordAuthentication':
  value => 'no',
}
