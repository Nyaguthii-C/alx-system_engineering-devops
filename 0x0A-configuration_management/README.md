
# Project: 0x0A. Configuration management
### Concepts
- **CI/CD**, **Scripting**, **SysAdmin**, **DevOps**
### Resources
[Intro to Configuration Management](https://intranet.alxswe.com/rltoken/GL30hu-aRcKzPOvK8JO-Bg)  
[Puppet resource type: file](https://intranet.alxswe.com/rltoken/WON0M4DNRabf88KAG_pDUA)(check “Resource types” for all manifest types in the left menu)  
[Puppet’s Declarative Language: Modeling Instead of Scripting](https://intranet.alxswe.com/rltoken/0V2fBdafkfKPMxA1umea3Q)  
[Puppet lint](https://intranet.alxswe.com/rltoken/CRUMeEMdcX-UtbWsUM9xLQ)  
[Puppet emacs mode](https://intranet.alxswe.com/rltoken/MzHXCntAkPzOqMnI6_rpWQ)
### Install puppet  
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades  
$ apt-get install -y ruby-augeas  
$ apt-get install -y ruby-shadow  
$ apt-get install -y puppet  
## Tasks  
- 0-create_a_file.pp - Using Puppet, create a file in /tmp
- 1-install_a_package.pp - Using Puppet, install flask version 2.1.0 from pip3
- 2-execute_a_command.pp - create a manifest that kills a process named killmenow using exec puppet resource
