# Vagrant Notes

[Getting Started with Vagrant](http://docs.vagrantup.com/v2/getting-started/index.html)

* install `vagrant-proxyconf` plugin [\[1\]][1]:  

```  
vagrant plugin install vagrant-proxyconf
```

* Install a box locally

  * Download a box (e.g., [precise32][2])
  * Be sure to add `mingw\bin` to your PATH variable
  * `vagrant box add hashicorp/precise32 <local_path_to_file>/precise32.box`

* Start up box and connect

  * `vagrant up`
  * `vagrant ssh` -- doesn't work in Windows unless you have `ssh` on your %PATH%
-----

[1]: http://stackoverflow.com/questions/19872591/how-to-use-vagrant-in-a-proxy-enviroment
[2]: https://vagrantcloud.com/hashicorp/boxes/precise32/versions/1
