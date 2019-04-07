Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  config.vm.network "forwarded_port", guest: 8001, host: 8001, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 80, host: 8002, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 8080, host: 8080

end
