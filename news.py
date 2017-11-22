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
    pass

def first_question():
    conn, cur = connect()
    cur.execute("select * from authors")
    question_one = cur.fetchall()[3][0]
    print question_one

first_question()
