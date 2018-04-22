# Homestead new project helper 

When using the official Laravel dev enviroment [Homestead](https://laravel.com/docs/5.6/homestead) there's a couple of steps you need to do
in order to set up a new project. This script seeks to automate some of them, it:
1. Creates a new folder for your project
2. Adds appropriate entries to the Homestead.yaml file
3. Adds the corresponding entry to your hosts file

To use first rename the config.example.txt file to config.txt and update it according to your setup.  
- HOSTS_FILE - location of your hosts file, default C:\Windows\System32\drivers\etc\hosts  
- PROJECTS_FOLDER - the projects folder on your local machine  
- REMOTE_PROJECTS_FOLDEr - the address of the projects folder on your homestead vm  
- ADDRESS - IP address of the homestead vm, default 192.168.10.10  
- DOMAIN - domain name extension you wish to use  
- HOMESTEAD_YAML - path to your homestead.yaml file  

Use  
```homesteadhelper myprojectname```

With the default config the above command would generate
- new folder C:\vagrant\homestead\code\public
- add to homestead.yaml : map: myprojectname.homestead to: /home/vagrant/code/myprojectname/public
- add to hosts: 192.168.10.10 myprojectname.homestead


Requires Python 3.6 and the PyYaml library.
