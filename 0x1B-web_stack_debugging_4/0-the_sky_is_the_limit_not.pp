#web stack debugging 4
exec { 'Correct file and restart':
  command  => "sudo echo 'ULIMIT=\"-n 4096\"' > /etc/default/nginx && sudo service nginx restart",
  provider => shell,
}
