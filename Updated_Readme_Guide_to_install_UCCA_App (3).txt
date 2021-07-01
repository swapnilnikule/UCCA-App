                                    Steps to install UCCA_App
####################################################################################################################

INSTALLATION GUIDE REFERENCE:   

https://github.com/omriabnd/UCCA-App/blob/master/INSTALLATION_GUIDE.md

LINK TO GITHUB REPO (UCCA_APP):

https://github.com/omriabnd/UCCA-App

OS Name: Ubuntu 20.04.1 LTS
#############################################################################################################

Prerequisite:

1) Docker CE
2) Docker compose

Link for reference(Docker CE):  https://docs.docker.com/engine/install/ 
Link for reference(Docker Compose): https://docs.docker.com/compose/install/
   

Installing docker ce

____Setting up the repo____

1. $ sudo apt-get update

2. $ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

3. $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

4. $ sudo apt-key fingerprint 0EBFCD88

5. $ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

__Installing engine___

6. $ sudo apt-get update

7. $ sudo apt-get install docker-ce 

8. $ sudo docker run hello-world


Install Docker Compose

1. sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

2. sudo chmod +x /usr/local/bin/docker-compose
		if this commands fails use 
	 sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

3. $ docker-compose --version

NOTE: if 3rd step fails use			#edited
      $ sudo docker-compose --version


#########################################################################################################################


Steps to install UCCA for EVALUATION purpose only 
(note: can only view already made annotations or cannot make any changes):

1) Download the zip file of UCCA_App from the github repo and unzip it.

2) open terminal and change directory to the UCCA-App-master/deployment/ where you unzipped
   or 
 just got to deployment inside the unzipped folder using file manager and right click and click open with terminal 

3) inside terminal 
	cmd:  docker-compose up

note: first time it will download docker images from dockerhub so will take time to download and get your container running.

4) your app will be live on http://localhost:6080


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Steps for installing UCCA for development purpose:
(Can add and make changes):

#_FRONTEND_

Installation guide for ucca-app to install frontend
(we faced issue with the version of nodejs do remember to use the given version other version may not work)

1. add path /usr/bin to PATH in the beginning so that it takes /usr/bin/curl for curl command instead of from anaconda envrironment

	which curl should point to /usr/bin/curl


2. Install nvm

	wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.36.0/install.sh | bash
	Close and reopen your terminal to start using nvm 

3. Install nodejs version 8.17 (later versions will not work)

	nvm install v8.17.0

	check the node version

	node --version
	v8.17.0


4. Install yarn

	remove the yarn other package by default installed in ubuntu

	sudo apt remove yarn

	curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
	echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

	sudo apt update && sudo apt install --no-install-recommends yarn

	Go to 'Client' directory inside ucca-app and run 'yarn install'
	It should end with out any error.

	cd Client
	yarn install

5. Install gulp

	Inside 'Client' directory run the following commands.

	cd Client

	npm install --global gulp-cli

	npm install --save-dev gulp

	check with  gulp -v


6. Run the Frontend


	Go to the client directory and run the following command.

	cd ../Client
	gulp serve

	It will open the frontend in the browser.
	
	url: http://localhost:3000/

Note: Dont close the terminal or stop the running commands 
 Open a new terminal to perform further steps let the server be running.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing DATABASE POSTGRES SQL

reference: https://www.postgresql.org/download/
version used: postgresql-12

(we faced issue with the authentication of postgres while running the backend 
so i listed the solution below changing the authentication token from peer and ident to trust on postgres)

# Create the file repository configuration:
$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
$ sudo apt-get update

# Install the 12 version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
$ sudo apt-get -y install postgresql-12

#enabling services to start database everytime the system is rebooted

1) $ systemctl start postgresql-12

NOTE:   if above command does not work then use this command:         #edited 
	$ sudo pg_ctlcluster 12 main start      
	

2) $ system enable postgresql-12

NOTE:	 if above command doesn't work use:		#edited 
 	  $ sudo pg_ctlcluster 12 main enable  

		
3) check using
   $ system is-enable postgresql-12
   
NOTE:     if above cmd doesn't work use	         	#edited by rahul
 	  $ sudo pg_ctlcluster 12 main status 
   
   
configuring the postgressql

1)	$ sudo su - postgres
create username and password for your postgres     #I have only created username and doesn't ask for password
						    #if asked you can give password to it.

2)	$ psql

3)Create a database with name ucca

postgres=# CREATE DATABASE ucca;

changing authentication permission

1) login to postgres user

$ sudo su - postgres

2) change directory

$ cd /etc/postgresql/12/main/pg_hba. conf     	     		#edited 

3) edit using any editor

$ gedit pg_hba.conf

NOTE: if error occurs by running gedit cmd, use vi cmd to edit it:		#edited 
      $ vi pg_hba.conf    	 
	
change all ident peer to trust 


# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     trust
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 trust
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     trust
host    replication     all             127.0.0.1/32            trust
host    replication     all             ::1/128                 trust

#### this is how the pg_hba.conf looks change all methods from ident peer to trust

save it 

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


BACKEND CONFIGURATION AND SETUP

(while installing requirements do note that conda may not contain all the packages required you can install it using pip mannually one by one)

1> CHANGE DIRECTORY TO SERVER (UCCA-App-master/Server)

$ cd ./Server

2> Install all the requirements given in requirements.txt file

	either by using pip3 or conda

	 create a environment (NOTE: mandatory to create virtual environment with python=3.6.8 to work properly) 
	 											#edited

	{
	  $conda create --name ucca python=3.6.8
	   $conda activate ucca
	}

$ pip3 install -r requirements.txt (mandatory)

(#edited by rahul)
If error occurs go through below note or else proceed to next step:	

Note:	(after installing above packages, error might occur such as "Building wheel for psycopg2 	      		(setup.py) ... error"). This is because python latest version doesn't support these packages so create 		virtual environment with python=3.6.8 using above step and then proceed.  
	  
	If still some error occur related to psycopg pakage use these command:
		$ sudo pip3 install psycopg2-binary" 
		$ sudo apt-get install libpq-dev		#edited 
	

	
	
	
3> copy settings_ucca_docker.py file in docker-helpers (path: UCCA-App-master/Server/docker-helpers) to ucca folder (path: UCCA-App-master/Server/ucca)

and rename the file in ucca (path: UCCA-App-master/Server/ucca) 
settings_ucca_docker.py >>>>to>>>> local_settings.py

$ cd ./docker-helpers
$ cp settings_ucca_docker.py ./ucca/local_settings.py      #You can also do this (copy-paste) in graphical way if 								   this not work.  

4> edit local_settings.py using any editor

change host name from  'HOST': 'ucca-db', to 'HOST': '0.0.0.0', 
0.0.0.0 is the ip on which docker postgres will be running 

save it

5> edit settings.py
edit from line 125 to 136

uncomment user and password and fill the password and user name you entered in postgres
hostname is your ip on which database is running it ususally local host 127.0.0.1 

This is the settings that I applied


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'options': '-c search_path=ucca'
        },
        'NAME': 'ucca',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

save it


################Running postgres on Docker#############


1> change directory to deployment (UCCA-App-master/deployment)
	$ cd ./deployment

2> run docker-compose

	$ sudo docker-compose --file docker-compose-db.yml up

Note: to perform further steps dont close the terminal or stop the running command use new terminal 
 
##############migrate data from docker postgres to postgres on system##########

1> go to server folder (UCCA-App-master/Server)

$ cd ./Server

2> $ python3 manage.py runserver               

( Note:use python3 or python whichever works in your system for running python files)

( after executing the command it will show in red line

You have 34 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): account, admin, auth, authtoken, contenttypes, sessions, sites, uccaApp.
Run 'python manage.py migrate' to apply them.

 )

3> apply migration

$ python manage.py migrate

(#edited by rahul)
NOTE:	Error might occur like below given. This is because my latest python version doesn't support these 		packages in requirements.txt file. So it is mandatory to have python=3.6.8 in your virtual env and error 	 should get solved)
     
        "RuntimeError: __class__ not set defining 'AbstractBaseUser' as <class 		'django.contrib.auth.base_user.AbstractBaseUser'>. Was __classcell__ propagated to type.__new__?"
	
	You can check django version by command:

	  $ python3 -m django --version)



4> load data files in local postgressql

$ python manage.py migrate
$ python manage.py loaddata tabs
$ python manage.py loaddata roles
$ python manage.py loaddata roles_tabs
$ python manage.py loaddata permissions
$ python manage.py loaddata groups_permissions_admin
$ python manage.py loaddata groups_permissions_guest
$ python manage.py loaddata groups_permissions_project_manager
$ python manage.py loaddata groups_permissions_annotator

$ python manage.py loaddata categories$ python manage.py loaddata layers
$ python manage.py loaddata layers_categories
$ python manage.py loaddata sources
$ python manage.py loaddata passages

5> Load Initial superuser to database 

$ python manage.py loaddata superuser

this will load a super user 
 user:    admin.ucca2@cs.huji.ac.il 
password: adminucca

refresh the front end page running in the browser
	url: http://localhost:3000/

#if it is working now you can close stop the docker postgres you dont need to run it any time now 



Thank YOu.....


