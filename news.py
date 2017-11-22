#!/usr/bin/env python3

import psycopg2

def connect(database_name="news"):
    try:
        conn = psycopg2.connect("dbname={}".format(database_name))
        cur = conn.cursor()
        return conn, cur
    except:
        print ("Error. Connection didn't work.")

def first_question():
    conn, cur = connect()
