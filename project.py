#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def getTopThreeArticles(conn):

    c = conn.cursor()
    c.execute('''
    SELECT
        title,count(log.path) AS views
    FROM
        articles,log
    WHERE
         log.path LIKE concat('%', articles.slug,'%')
         AND log.status NOT LIKE '%404%'
         GROUP BY articles.title
         ORDER BY views DESC
         LIMIT 3;
     ''')
    results = c.fetchall()
    print("Question 1: ")
    for row in results:
        print('"{}" - {} Views').format(row[0], row[1])


def getMostPopularAuthor(conn):
    c = conn.cursor()
    c.execute('''
    SELECT
        name,count(log.path) AS views
    FROM
         articles,authors,log
    WHERE
        articles.author = authors.id
        AND log.path LIKE concat('%', articles.slug,'%')
        AND log.status NOT LIKE '%404%'
        GROUP BY name
        ORDER BY views DESC;
     ''')
    results = c.fetchall()
    print("Question2: ")
    for row in results:
        print('{} - {} Views').format(row[0], row[1])


def getTopErrorDay(conn):
    # This method requires 2 Views that are included in the Readme.md File
    c = conn.cursor()
    c.execute('''
    SELECT
         AllRequests.date,
         (100*Cast(FaultyRequests.result as Float) /AllRequests.result)
         AS percentage
    FROM
         AllRequests,FaultyRequests
    WHERE
          FaultyRequests.date=AllRequests.date
          ORDER BY percentage desc
          LIMIT 1;
    ''')
    results = c.fetchall()
    print("Question 3: ")
    for row in results:
        date = row[0].strftime("%b %d, %Y")
        print('{} - {}% errors'.format(date, row[1]))


if __name__ == '__main__':
    try:
        conn = psycopg2.connect(database=DBNAME)
    except:
        print("Unable to connect to the database")

    getTopThreeArticles(conn)
    getMostPopularAuthor(conn)
    getTopErrorDay(conn)
