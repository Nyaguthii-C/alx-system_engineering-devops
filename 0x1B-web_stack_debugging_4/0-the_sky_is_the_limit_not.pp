# puppet file to configure server to accept 2000 requests
# onlyif to check whether the current ULIMIT value
# is different from desired value, Idempotence

exec {'replace' :
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/" /etc/default/nginx',
  onlyif   => "grep -qE '^ULIMIT=\"-n .*\"$' /etc/default/nginx",
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
