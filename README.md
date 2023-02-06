## IvyLog_app
Repo to store files used to develop Ivy project for test

##Ivy_log_application

The application is to provide user experience of a product to monitor the daily activity of the devices installed at their premises. It has been developed using python and Flask framework for the endpoint and hosted on Amazon AWS.

## Installation
1.	If Python is not installed, please install Python.
2.	Install pip using 
    Python3 -m pip install
3.	Install mysqldump tool
    For Ubuntu-based Linux systems
    sudo apt install mysql-client
4.  Once installed, use mysqldump to create schema and load the tables.
    mysql -h [your DB host's name or IP] -u [your DB user's name] -p [your db password] < SQL data/sqldatadump.sql
5.  Rename src/credentials_example.py to credentials.py and add your mysql crdentials

## Running the application
1.	To start the application locally run below command.
             bash setup.sh
             


             




