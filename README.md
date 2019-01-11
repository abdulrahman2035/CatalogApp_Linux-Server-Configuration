# Project: Udacity Full Stack Web Developer Project 5  Linux Server Configuration

#Project description
 on this project we will work on configuration and setup a linux server to deploy Catalog App Project.
 You can visit http://18.184.184.127.xip.io/ for the App deployed on AWS.  
 

#Udacity Reviewer
 SSH Address: 18.184.184.127
 SSH Port: 2200
 UserAccount: grader
 Password:1234
 
#Summary of software you installed
 1-sudo apt-get update
 2-sudo apt-get install python-pip 
 3-sudo apt-get install python3-pip
 4-sudo apt-get install python-flask 
 5-sudo apt-get install apache2 
 6-sudo apt-get install libapache2-mod-wsgi
 7-sudo apt-get install python3-pip
 8-sudo apt-get install libapache2-mod-wsgi
 9-sudo apt-get install libapache2-mod-wsgi
 10-sudo apt-get install python-setuptools
 11-sudo apt-get install postgresql
 12-sudo apt-get install git


# Configuration implementation and steps :
1-Launch The Virtual Machine.

2-Follow the instructions provided to SSH into your server
 a. by using the Private Key 
 b. using putty app to access to the server you can downloaded from here : https://www.putty.org/
 c.open the putty app and from the left side menu click on ssh then auth then  browse to select the private kay.
 d.from the left side menu click on session then put the ip of the instance: host: 18.184.184.127, username: grader then click open 

 
3- Create a new user named grader and give hem permission to sudo 

    a. sudo adduser grader
    b. vim /etc/sudoers
    c. touch /etc/sudoers.d/grader
    d. vim /etc/sudoers.d/grader, type in grader ALL=(ALL:ALL) ALL, save and quit

4-Set SSH login using the keys
   a.generate keys on local machine usingssh-keygen  then save the private key in ~/.ssh on the local machine

   b.deploy public key on developement enviroment

      On you virtual machine:

      $ su - grader
      $ mkdir .ssh
      $ touch .ssh/authorized_keys
      $ vim .ssh/authorized_keys

      Copy the public key generated on your local machine to this file and save

      $ chmod 700 .ssh
      $ chmod 644 .ssh/authorized_keys

    c.reload SSH using service ssh restart

    d.now you can use ssh to login with the new user you created

       ssh -i key grader@18.184.184.127


5.Update all currently installed packages by using the bellow commands:
  a.sudo apt-get update
  b.sudo apt-get upgrade
 
 
 
 6.Change the SSH port from 22 to 2200 by using the bellow commands:
 
  a. Use sudo vim /etc/ssh/sshd_config and then change Port 22 to Port 2200 then  save and quit
  b. Reload SSH using: sudo service ssh restart.


7.Configure the Uncomplicated Firewall
 Configure the Uncomplicated Firewall to only allow the incoming connections for SSH port 2200 and HTTP port 80 and NTP port 123 by using the below commands: 
  a.sudo ufw allow 2200/tcp
  b.sudo ufw allow 80/tcp
  c.sudo ufw allow 123/udp
  d.sudo ufw enable 


8.Configure the local timezone to UTC by using the bellow commands:
 a.Configure the time zone sudo dpkg-reconfigure tzdata


9.Install and configure Apache to serve a Python mod_wsgi application by using the below commands: 
  1-Install Apache sudo apt-get install apache2
  2-Install mod_wsgi sudo apt-get install python-setuptools libapache2-mod-wsgi
  3-Restart Apache sudo service apache2 restart
  4-sudo ufw allow 'Apache Full'
  
10.Install and configure the PostgreSQL by using the below instructions: 

   a.Install PostgreSQL using: sudo apt-get install postgresql

   b.Check if no remote connections are allowed sudo vim /etc/postgresql/9.3/main/pg_hba.conf

   c.Login as user "postgres" sudo su - postgres

   d.Get into postgreSQL shell psql
   e.Create a new database named catalog and create a new user named catalog in postgreSQL shell
      1.postgres=# CREATE DATABASE catalog;
      2.postgres=# CREATE USER catalog;
 
   f.Set a password for user catalog
      postgres=# ALTER ROLE catalog with the password ;

   g.Give user "catalog" permission to "catalog" application database
    postgres=# GRANT ALL PRIVILEGES ON DATABASE catalog TO catalog;

   h.Quit postgreSQL 
    postgres=# \q  then exit. 


11.installing git,clone and setup the CatalogApp            

    a. Install Git using sudo apt-get install git
    b. Use cd /var/www to move to the /var/www directory
    3-Create the application directory sudo mkdir CatalogApp - the final path of the project folder should be /var/www/CatalogApp/CatalogApp
    4-Move inside this directory using cd CatalogApp
    5-Clone the CatalogApp to the virtual machine git clone https://github.com/abdulrahman2035/CatalogApp_Linux-Server-Configuration.git
    Rename the project name sudo mv ./CatalogApp ./CatalogApp
    Move to the inner CatalogApp directory using cd CatalogApp
    Rename app.py to application.py using sudo mv website.py application.py
	Edit application.py and change client_secrets.json to /var/www/CatalogApp/CatalogApp/client_secrets.json
    Install pip sudo apt-get install python3-pip 
    Use pip to install dependencies sudo pip3 install -r requirements.txt
    Install psycopg2 sudo apt-get -qqy install postgresql python-psycopg2
    Create database schema sudo python3 database_setup.py



12.Configure and Enable a New Virtual Host
 a.Create CatalogApp.conf to edit: sudo nano /etc/apache2/sites-available/CatalogApp.conf.
 b.Add the following lines of code to the file to configure the virtual host.

    <VirtualHost *:80>
	ServerName 18.184.184.127
	ServerAdmin Hello_World@gmail.com   
	WSGIScriptAlias / /var/www/CatalogApp/CatalogApp.wsgi
	<Directory /var/www/CatalogApp/CatalogApp>
		Order allow,deny
		Allow from all
	</Directory>
	Alias /static /var/www/CatalogApp/CatalogApp/static/
	<Directory /var/www/CatalogApp/CatalogApp/static>
		Order allow,deny
		Allow from all
	</Directory>
	ErrorLog ${APACHE_LOG_DIR}/error.log
	LogLevel warn
	CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>

 3-Enable the virtual host with the following command: sudo a2ensite CatalogApp

 13.Create the .wsgi File
   1-Create the .wsgi File under /var/www/CatalogApp/CatalogApp:
       1.cd /var/www/CatalogApp/CatalogApp
       2.sudo nano CatalogApp.wsgi
	   
   2-Add the following lines of code to the CatalogApp.wsgi file:
   
      #!/usr/bin/python
    import sys
    import logging
    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0,"/var/www/CatalogApp/CatalogApp")

    from CatalogApp import app as application
	application.root_path = '/var/www/CatalogApp/CatalogApp'
	application.secret_key = 7uJB826hk2ltUZmdsYbsGHiN


   14.Restart Apache and run the CatalogApp
    a. sudo service apache2 restart



	List of third-party resources that help me on these configurations : 
	a.stack overflow.
	b.Google search engine.
	c.http://flask.pocoo.org/docs/1.0/deploying/







