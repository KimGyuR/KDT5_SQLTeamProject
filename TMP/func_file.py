import pandas as pd
import matplotlib.pyplot as plt
import pymysql

def executeSQL(conn, cur, sql):
    try:
        cur.excute(sql)
    except Exception as e:
        print('Error detected :', e)


def makeDF(conn, cur, table):
    try:
        sql = 'select * from ' + table
        cur.execute(sql)
        data = cur.fetchall()
        return pd.DataFrame(data)
    except Exception as e:
        print('Error detected :', e)
        return None

def drawPlot(x, y):
    plt.figure(figsize=(12, 3))
    plt.plot(x, y)
    plt.show()