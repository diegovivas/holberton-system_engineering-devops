#install ngnx
exec { 'instal_ngnx':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx &&
  echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html &&
  sudo service nginx start',
  provider => 'shell',
}

