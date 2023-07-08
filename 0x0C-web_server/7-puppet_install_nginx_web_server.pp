#install Nginx
class nginx {
  package { 'nginx':
    ensure => installed,
  }
#start Nginx

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
#redirection, port config, page

  file { '/etc/nginx/sites-enabled/default':
    ensure  => present,
    content => '
      server {
        listen 80;
        server_name _;

        location / {
          return 301 https://help.dreamhost.com/hc/en-us/articles/216456087-Creating-redirects-with-Nginx;
        }

        location / {
          root /var/www/html;
          index index.html;
	}
      }
    ',
    notify  => Service['nginx'],
  }
}

include nginx

