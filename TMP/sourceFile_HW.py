import pandas as pd
import matplotlib.pyplot as plt
import pymysql
import func_file as ff

conn = pymysql.connect(
    host='175.122.58.102',
    port=33063,
    user='KMS',
    password='1234Q1@',
    db='ProjectDB',
    charset='utf8',
)

cur = conn.cursor()

tableList = ['GHW_ability_toy',
             'GHW_production_education',
             'GHW_production_toy']

atDF = ff.makeDF(conn, cur, tableList[0])
peDF = ff.makeDF(conn, cur, tableList[1])
ptDF = ff.makeDF(conn, cur, tableList[2])

print(atDF)
# print(peDF)
# print(ptDF)
print(atDF[1])

# ff.drawPlot(atDF[1], atDF[2])

conn.close()
cur.close()
