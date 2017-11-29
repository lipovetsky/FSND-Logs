# FSND-Logs-Analysis

When you're in charge of a website, you may choose to
install some kind of analytics software. This will
help you to determine which of your web pages are the
most popular, which are the least popular, where your users
are going, and where your users are running into error pages.
This program analyzes these analytics using an SQL database.
It returns plain text queries that are much easier to read
than going into the database and trying to look at the
numbers yourself. There are over 1 million rows! Thank
goodness for Python and SQL!

## Install the Database

This code assumes that you already have the humongous
newsdata.sql file on your machine. First, you must add
the news.py file to the same exact folder where newsdata.sql
is located.

Then, we need to install the news database. To do this,
you will need to have a machine with some kind of SQL
running. I used Vagrant with PostreSQL pre-installed.
Shout out to Udacity for helping us out in the Full
Stack Nanodegree, of which this is a project.

Once you are in the directory on your terminal,
and have PostreSQL running, use this command
to create the database


`$ psql -d news -f newsdata.sql.`

## Run the Script

The hard part is over. Now, all we have to do
is run the Python3 script! If you don't have
Python3 installed, try running this on
your terminal:

`$ brew install python3`

If that doesn't work, you need to install
homebrew. Check the following site for more:

[http://docs.python-guide.org/en/latest/starting/install3/osx/]

Now that we have Python3 installed, all we
have to do is run the following command:

`python3 news.py`

Sit back, relax, and enjoy.
The database is doing all of the heavy lifting.


## Concluding Words

This project was created as part of the Full Stack
Nanodegre for Udacity. You will learn A LOT about
SQL, should you choose to enroll. Recommended!
