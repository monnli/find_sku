# -*- coding: utf-8 -*-
import pymysql


def tidb_conn():
    conn = pymysql.connect(
        host='172.31.141.244',
        port=31545,
        user='similarity',
        password='ye6Iep8S',
        db='voila_similarity'
    )
    cursor = conn.cursor()
    return cursor, conn
