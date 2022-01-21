package {'vi':
 ensure => installed,
}
package {'mc':
 ensure => installed,
}
package {'wget':
 ensure => installed,
}
package {'tar':
 ensure => installed,
}
package {'bind-utils':
 ensure => installed,
}
package {'net-tools':
 ensure => installed,
}
package {'telnet':
 ensure => installed,
}

package {'tcpdump':
 ensure => installed,
}

package {'curl':
 ensure => installed,
}

firewalld_port { 'Open port 80 in the public zone':
  ensure   => present,
  zone     => 'public',
  port     => 80,
  protocol => 'http',
}

firewalld_port { 'Open port 443 in the public zone':
  ensure   => present,
  zone     => 'public',
  port     => 443,
  protocol => 'https',
}

service { 'sshd' :
  ensure => 'running';
}

augeas { "Disable_Root_Login":

       context => "/files/etc/ssh/sshd_config",

       changes => "set PermitRootLogin no",

       notify    =>  Service['sshd']

}


