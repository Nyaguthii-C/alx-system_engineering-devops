# using Puppet to make changes to configuration file to connect to a server without typing a password

file_line {' declare identity fiile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/school',
}

file_line {'refuse authentication using password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
