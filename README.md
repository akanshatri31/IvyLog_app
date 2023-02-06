## IvyLog_app
Repo to store files used to develop Ivy project for test

##Ivy_log_application

The application is to provide user experience of a product to monitor the daily activity of the devices installed at their premises. It has been developed using python and Flask framework for the endpoint and hosted on Amazon AWS.

To reach the application, please click below:
http://ec2-18-170-118-201.eu-west-2.compute.amazonaws.com/get_logs

## Installation
1.	If Python is not installed, please install Python.
2.	Install pip using 
    Python3 -m pip install
3.	Install mysqldump tool
    For Ubuntu-based Linux systems
    sudo apt install mysql-client
4.  Once installed, use mysqldump to get a full backup of a database.
    mysqldump -h [your DB host's name or IP] -u [your DB user's name] -p [your db password] >       (https://github.com/akanshatri31/IvyLog_app/blob/main/SQL%20Data/sqldatadump)

## Running the application
1.	To start the application locally run below command.
             bash src/https://github.com/akanshatri31/IvyLog_app/blob/main/setup.sh
             
## Testing
1.  End point: get_logs
    Type in your browser: http://ec2-18-170-118-201.eu-west-2.compute.amazonaws.com/get_logs
    Test case: To show logs when customer logins without search, pageno and filter option.
    Expected result: Fetch first 20 records in descending order of date and grouped by date.
2.  End point: get_logs?&page=
    Type in your browser: http://ec2-18-170-118-201.eu-west-2.compute.amazonaws.com/get_logs?&page=2
    1.  Test case: To show logs and load more logs (use page no to navigate)
        Parameter => Page = 2
        Expected result: For Page=2, fetch next 20 records in descending order of date and grouped by date.
    2.  Test case: To show logs and load more logs (use page no to navigate)
        Parameter => Page = 20
        Expected result: For Page=20, fetch next 20*(20-1) records in descending order of date and grouped by date. 
    3. Test case: To show logs and load more logs (use page no to navigate)
        Parameter => Page = 26
        Expected result: For Page=26, No more result found or End of the logs.
3. End Point: get_logs?&event
    
    
    
             




