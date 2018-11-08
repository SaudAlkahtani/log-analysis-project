## This project is presented for Udacity Full stack nano degree 
### This project is used to analyse a database/log  of a news website.
#### The Queries that the code do is:
- What is the top 3 Viewed Articles?.
- Which authors has the most viewed Articles?
- Which day has more than 1% of errors in requesting the pages 
### Content of the database
#### The database has three tables
- Authors Table
  - Includes these columns :
    - name of the author.
    - id of the author.
    - his bio.
-  Articles Table
   - Includes these columns:
     - The id of the article's author.
     - The article's title.
     -  The article's slug which appears in the uri
     - The lead of the article
     - The body of the article
     - The time it was posted
     - The article's id 
- Log table
  - Includes these columns:
    - The id of the request 
    - The path of the request
    - The ip which requested the article
    - The method used to access it (get,post)
    - The status of request(200 ok , 404 not found)
    - Time of the request
    - Id of the request
## Steps you need to run this code:
 - Install the required software:
   - a.Vagrant: https://www.vagrantup.com/downloads.html
   - b. Virtual Machine: https://www.virtualbox.org/wiki/Downloads
   - c. Download a FSND virtual machine: https://github.com/udacity/fullstack-nanodegree-vm
 - Once installed, download the project.py, and the database from : https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdat a.zip
   after downloading the files, put them in your vagrant file, and then,
   using your prefered command line , use the following commands:
   ```
    cd vagrant
    vagrant up 
    vagrant ssh
    cd /vagrant
   ```

- Once you're there you need to add views to your postqrese sql by doing :
    ```
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
     ```       
    - now you're ready to execute the program 
    enter "`\q`" to exit out of the psql , 
    then enter "`pip3 project.py`" 
The project should be excuted and you should get the results as shown in Output.txt
