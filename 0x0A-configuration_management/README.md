
# Project: 0x0A. Configuration management
### Concepts
- **CI/CD**, **Scripting**, **SysAdmin**, **DevOps**
### Install puppet  
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades  
$ apt-get install -y ruby-augeas  
$ apt-get install -y ruby-shadow  
$ apt-get install -y puppet  
## Tasks  
- 0-create_a_file.pp - Using Puppet, create a file in /tmp
- 1-install_a_package.pp - Using Puppet, install flask version 2.1.0 from pip3
- 2-execute_a_command.pp - create a manifest that kills a process named killmenow using exec puppet resource
