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
    try:
        conn, cur = connect()
        cur.execute('''
        create view okstatus as
        select count(status),
        time::DATE as date
        from log
        where status = '200 OK'
        group by date
        order by date;
        ''')
        cur.execute('''
        create view badstatus as
        select count(status),
        time::DATE as date
        from log
        where status != '200 OK'
        group by date
        order by date;
        ''')
        conn.commit()
        conn.close()
    except psycopg2.Error:
        pass


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
    1. "{}" - {} views \n
    2. "{}" - {} views \n
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
    1. {} - {} views \n
    2. {} - {} views \n
    3. {} - {} views \n
    4. {} - {} views \n""".format(question_two[0][0], question_two[0][1],
    question_two[1][0], question_two[1][1],
    question_two[2][0], question_two[2][1],
    question_two[3][0], question_two[3][1]))
    conn.close()

def third_question():
    conn, cur = connect()
    cur.execute('''
    select okstatus.count, badstatus.count, okstatus.date
    from okstatus, badstatus
    order by okstatus.date;
    ''')

    cur.execute('''
    select a.time::DATE, count(yo)
    from log a, log b,
    (
    select a.time::DATE, count(a.status) as yo
    from log a
    where a.status = '200 OK'
    group by a.time::DATE) as goodviews
    where a.id = b.id
    group by a.time::DATE;

    select distinct a.time::DATE,
    count(a.status) as OK,
    count(b.status) as BAD
    from log a, log b
    where a.id = b.id
    group by a.time::DATE, a.status, b.status
    having a.status = '200 OK'
    or b.status != '200 OK'
    order by a.time::DATE;
    ''')

    cur.execute('''
    select a.time::DATE, count(a.status) as OK,
    count (a.status) as ERROR
    from log a JOIN log b
    on a.id = b.id
    and a.status <> '200 OK'
    group by a.time::DATE;
    ''')

join with Log c!!
    conn.close()

where b.status <> '200 OK'
and c.status <> '200 OK'








create_views()
first_question()
second_question()
third_question()
