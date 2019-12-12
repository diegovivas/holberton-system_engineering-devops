#install ngnx
exec { 'instal_ngnx':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx &&
  echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html &&
  var1="server_name _;\n\t rewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;"
  && sudo sed -i "s/server_name _;/$var1/" /etc/nginx/sites-enabled/default && sudo service nginx start',
  provider => 'shell',
}

