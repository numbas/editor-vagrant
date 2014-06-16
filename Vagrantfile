# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise32"

  config.vm.provision :shell, path: "setup/provision.sh"

  config.vm.network :forwarded_port, host: 4567, guest: 80

  config.vm.post_up_message = "All done! The editor is accessible at http://localhost:4567. The admin is username 'admin' with password 'admin'."
end
