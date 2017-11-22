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
    question_one = cur.fetchall()[3][0]
    print ("The three most popular articles of all time are:" + question_one[1])

first_question()
