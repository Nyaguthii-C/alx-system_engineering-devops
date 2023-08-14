# puppet file to configure server to accept 2000 requests

exec {'replace' :
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/" /etc/default/nginx'
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
