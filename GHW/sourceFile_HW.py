import pandas as pd
import matplotlib.pyplot as plt
import pymysql
import func_file as ff
import koreanize_matplotlib
from copy import deepcopy as dp

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
             'GHW_production_toy',
             'KMS_유치원',
             'KMS_초등학교']

atDF = ff.makeDF(conn, cur, tableList[0])
peDF = ff.makeDF(conn, cur, tableList[1])
ptDF = ff.makeDF(conn, cur, tableList[2])

kinderDF = ff.makeDF(conn, cur, tableList[3])
elementDF = ff.makeDF(conn, cur, tableList[4])

# print(elementDF[0].unique())
# print(elementDF[1].unique())
# print(elementDF[2].unique())
# print(elementDF[3].unique())
# print(kinderDF[1].unique())
# print(kinderDF[2].unique())
# print(kinderDF[3].unique())

totalKinderDF = dp(kinderDF[(kinderDF[0] == '전국') & (kinderDF[1] == '계') & (kinderDF[2] == '원아수 (명)') & (kinderDF[3] == '소계')])
totalelementDF = dp(elementDF[(elementDF[0] == '전국') & (elementDF[1] == '계') & (elementDF[2] == '학생수 (명)') & (elementDF[3] == '소계')])

# print(totalKinderDF)
# print(totalelementDF)

# print(atDF)
# print(peDF)
# print(ptDF)
# print(atDF[1])

atDF.drop(columns=[0], inplace=True)
atDF.columns = ['년도', '생산능력지수', '가동지수']

peDF.drop(index=10, columns=[0], inplace=True)
peDF.columns = ['년도', '유아교육기관', '초등교육기관', '중등교육기관', '고등교육기관', '학원']

ptDF.drop(columns=[0,1], inplace=True)
ptDF.columns = ['년도', '생산지수', '제품출하지수', '제품재고지수']

totalKinderDF.drop(columns=[0, 1, 2, 3], inplace=True)
totalKinderDF.columns = ['년도', '유치원아수']

totalelementDF.drop(columns=[0, 1, 2, 3], inplace=True)
totalelementDF.columns = ['년도', '초등학생수']

totalCRDF = pd.merge(totalKinderDF, totalelementDF, how='inner', on='년도')

# print(totalKinderDF)
# print(totalelementDF)
# print(totalCRDF)

# print(atDF)
# print(peDF)
# print(ptDF)
# print(atDF[1])

ff.drawPlot(atDF['년도'], atDF[['생산능력지수', '가동지수']], ['생산능력지수', '가동지수'])
ff.drawPlot(ptDF['년도'], ptDF[['생산지수', '제품출하지수', '제품재고지수']], ['생산지수', '제품출하지수', '제품재고지수'])
ff.drawTwinX(peDF['년도'], peDF[['유아교육기관', '초등교육기관', '학원']],
             totalCRDF['년도'], totalCRDF['유치원아수'], totalCRDF['초등학생수']
              )

conn.close()
cur.close()
