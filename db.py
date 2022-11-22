import pymysql

def get_connection_mysql():

    return pymysql.connect(
        host='localhost',
        user='root',
        password='Root123...',
        db='blog1')