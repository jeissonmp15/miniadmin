import mysql.connector


def connect_db():
    cnx = mysql.connector.connect(
        user='admin', password='eTDmD5bjohSvyu3NJhJv', host='miniadmin.czsrhdzsjubw.us-east-1.rds.amazonaws.com',
        database='adminsat'
    )

    return cnx


def close_connection(cursor, cnx):
    cursor.close()
    cnx.close()
