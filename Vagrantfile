# -*- mode: ruby -*-
# vi: set ft=ruby :


Adapter = `ip route | awk '/^default/ {printf $5}'`
IP = `ip route | cut -d"." -f1,2,3| awk '/^default/ {printf $3}'`
IMAGE_NAME = "bento/ubuntu-20.04"
N = 2
Hostname = "loket0"

Vagrant.configure("2") do |config|
	config.ssh.insert_key = false

	config.vm.provider "virtualbox" do |vb|
		vb.memory = 2000
		vb.cpus = 2
	end

	config.vm.define "loket-master" do |master|
		master.vm.define "loket-master"
		master.vm.box = IMAGE_NAME
		master.vm.network "public_network", bridge: "#{Adapter}", ip: "#{IP}.80"
		master.vm.hostname = "loket-master"
		master.vm.provision "ansible" do |ansible|
			ansible.playbook = "master-playbook.yml"
			ansible.extra_vars ={
				node_ip: "#{IP}.80",
				node_name: "loket-master",
				ansible_python_interpreter:"/usr/bin/python3",
			}
		end
	end

	(1..N).each do |i|
		config.vm.define "loketnode-#{i}" do |node|
			node.vm.define "loketnode-#{i}"
			node.vm.box = IMAGE_NAME
			node.vm.network "public_network", bridge: "#{Adapter}", ip:"#{IP}.#{80+i}"
			node.vm.hostname = "loketnode-#{i}"
			node.vm.provision "ansible" do |ansible|
				ansible.playbook = "node-playbook.yml"
				ansible.extra_vars = {
					node_ip:"#{IP}.#{80+i}",
					ansible_python_interpreter:"/usr/bin/python3",
				}
			end
		end
	end
end


