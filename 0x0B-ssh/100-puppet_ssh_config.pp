# using Puppet to make changes to configuration file to connect to a server without typing a password
include stdlib

file_line { ' declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentifyFile ~/.ssh/school',
}

file_line { 'refuse authentication using password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}
