#!/usr/bin/env python3

import psycopg2

def connect():
    try:
        conn = psycopg2.connect("dbname=news")
        cur = conn.cursor()
        return conn, cur
    except:
        "Could not connect."

def create_views():
    conn, cur = connect()
    pass
    cur.execute('''
    create view articleviews as
    ''')
    conn.commit()
    conn.close()


def first_question():
    conn, cur = connect()
    cur.execute('''select articles.title, count(log.path) as views
    from articles, log where status = '200 OK' and log.path like concat('%',articles.slug,'%')
    group by articles.title order by views desc;
    ''')
    question_one = cur.fetchall()
    print ("""The three most popular articles of all time are: \n
    1. {} - {} views \n
    2. {} - {} views \n
    3. {} - {} views \n""".format(question_one[0][0], question_one[0][1],
    question_one[1][0], question_one[1][1],
    question_one[2][0], question_one[2][1]))

first_question()
