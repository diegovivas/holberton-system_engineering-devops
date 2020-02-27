#web stack debugging 4
exec { 'Correct file and restart':
  command  => 'sudo echo 'ULIMIT="-n 2000"'> /etc/default/nginx && sudo nginx restart',
  provider => shell,
}
