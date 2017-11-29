#!/usr/bin/env python3

import psycopg2
import datetime


def connect():
    try:
        conn = psycopg2.connect("dbname=news")
        cur = conn.cursor()
        return conn, cur
    except:
        "Could not connect."


def first_question():
    conn, cur = connect()
    cur.execute('''select articles.title,
    count(log.path) as views
    from articles, log
    where status = '200 OK'
    and log.path like concat('%',articles.slug,'%')
    group by articles.title
    order by views desc;
    ''')
    question_one = cur.fetchall()
    print ("""\nThe three most popular articles of all time are: \n
    1. "{}" - {} views
    2. "{}" - {} views
    3. "{}" - {} views \n""".format(question_one[0][0], question_one[0][1],
                                    question_one[1][0], question_one[1][1],
                                    question_one[2][0], question_one[2][1]))
    conn.close()


def second_question():
    conn, cur = connect()
    cur.execute('''select authors.name,
    count(log.path) as views
    from articles, authors, log
    where articles.author = authors.id
    and status = '200 OK'
    and log.path like concat('%',articles.slug,'%')
    and articles.author = authors.id
    group by authors.id
    order by views desc;
    ''')
    question_two = cur.fetchall()
    print ("""The most popular authors are: \n
    1. {} - {} views
    2. {} - {} views
    3. {} - {} views
    4. {} - {} views \n""".format(question_two[0][0], question_two[0][1],
                                  question_two[1][0], question_two[1][1],
                                  question_two[2][0], question_two[2][1],
                                  question_two[3][0], question_two[3][1]))
    conn.close()


def third_question():
    conn, cur = connect()
    cur.execute('''
    select * from
    (select (blue.date) as date,
    (blue.error::decimal / (blue.ok + blue.error)) as result
    from
    (select a.time::DATE as DATE, count(b.status) as OK,
    count (c.status) as ERROR
    from log a
    LEFT JOIN log b
    on a.id = b.id
    and a.status = '200 OK'
    LEFT JOIN log c
    on a.id = c.id
    and a.status <> '200 OK'
    group by a.time::DATE) as blue) as blue2
    where blue2.result >= .01;
    ''')
    question_three = cur.fetchall()
    love = question_three[0][0].strftime("%B %d, %Y")
    print ("""The days where more than 1% of the requests led to errors: \n
    1. {} - {}% errors
    """.format(love, round(question_three[0][1] * 100, 1)))
    conn.close()

first_question()
second_question()
third_question()
