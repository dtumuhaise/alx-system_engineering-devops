# manifest that kills a process named killmenow

exec { 'kill_killmenow':
  command => '/usr/bin/pkill -f "killmenow"',
}
