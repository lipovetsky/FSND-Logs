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
    try:
        cur.execute('''
        create view articleviews as
        select articles.title,
        count(log.path) as views
        from articles, log where status = '200 OK'
        and log.path like concat('%',articles.slug,'%')
        group by articles.title order by views desc;
        ''')
        conn.commit()
        conn.close()
    except psycopg2.Error:
        pass

    try:
        cur.execute('''
        create view popularauthors as
        select authors.name,
        count(log.path) as views
        from articles, authors, log
        where articles.author = authors.id
        and status = '200 OK'
        and log.path like concat('%',articles.slug,'%')
        and articles.author = authors.id
        group by authors.id
        order by views desc;
        ''')
        conn.commit()
        conn.close()
    except psycopg2.Error:
        pass

def first_question():
    conn, cur = connect()
    cur.execute('select * from articleviews;')
    question_one = cur.fetchall()
    print ("""\nThe three most popular articles of all time are: \n
    1. {} - {} views \n
    2. {} - {} views \n
    3. {} - {} views \n""".format(question_one[0][0], question_one[0][1],
    question_one[1][0], question_one[1][1],
    question_one[2][0], question_one[2][1]))

def second_question():
    conn, cur = connect()
    cur.execute('''select articleviews.*
    from articleviews join authors where authors.id = articles.author
    group by articles.author;
    ''')
    question_two = cur.fetchall()


create_views()
first_question()
