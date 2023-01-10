# Using Puppet, install flask from pip3

class { 'python': }

python::pip { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
