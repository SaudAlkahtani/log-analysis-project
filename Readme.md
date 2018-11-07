This project is presented for FSND
Steps you need to run this code:
 Install the required software:
    a.Vagrant: https://www.vagrantup.com/downloads.html
    b. Virtual Machine: https://www.virtualbox.org/wiki/Downloads
    c. Download a FSND virtual machine: https://github.com/udacity/fullstack-nanodegree-vm
 Once installed, download the project.py, and the database from : https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdat a.zip
 after downloading the files, put them in your vagrant file, and then,
 using your prefered command line , use the following commands:
    cd vagrant
    vagrant up 
    vagrant ssh
    cd /vagrant
Once you're there you need to add views to your postqrese sql by doing :
    psql -d news
    create view FaultyRequests as 
            select 
                Date(time) as date ,count(*) as result
            from
                 log 
            where
                 status like '%404%'
            group by date;
    create view AllRequests as 
            select 
                Date(time) as date , count(*) as result
            from 
                log
            group by date;
    now you're ready to execute the program 
    enter "\q" to exit out of the psql , 
    then enter "pip3 project.py" 
The project should be excuted and you should get the results as shown in Output.txt
