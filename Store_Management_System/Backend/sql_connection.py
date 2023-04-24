import mysql.connector

__cnx = None   ### check for multiple connections

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Myrysen7',
                                  host='127.0.0.1',
                                  database='gs')
    return __cnx