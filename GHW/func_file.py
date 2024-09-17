import pandas as pd
import matplotlib.pyplot as plt
import pymysql
import koreanize_matplotlib

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


def drawPlot(xdata, ydata, cols=''):
    # text = textMaker(cols)
    plt.figure(figsize=(12, 4))
    plt.plot(xdata, ydata, marker='o')
    plt.title(label='연도별 인형, 장난감 및 오락기구 생산지수', fontsize=18)
    plt.xlabel('연도', fontsize=13)
    plt.ylabel('생산지수', fontsize=13)
    plt.legend(cols)
    plt.xticks(ticks=xdata, rotation=45, fontsize=11)
    plt.yticks(rotation=30, fontsize=11)
    plt.grid(alpha=0.35)
    plt.tight_layout()
    plt.show()

def drawTwinX(xdata1, ydata1, xdata2, ydata2_1, ydata2_2, cols=''):
    # text = textMaker(cols)
    tick1 = [ i-0.1 for i in xdata2 ]
    tick2 = [ i+0.1 for i in xdata2 ]

    plt.rcParams['figure.figsize'] = (12, 5)
    fig, ax1 = plt.subplots()
    ax1.plot(xdata1, ydata1, marker='o')

    ax2 = ax1.twinx()
    ax2.bar(tick1, ydata2_1, alpha=0.35, width=0.3)
    ax2.bar(tick2, ydata2_2, alpha=0.35, width=0.3)

    ax1.set_title(label='연도별 원아/학생수 대비 생산지수', fontsize=18)
    ax1.set_xlabel('연도', fontsize=13)
    ax1.set_ylabel('생산지수', fontsize=13)
    ax1.set_xticks(ticks=xdata1)
    ax1.legend(ydata1.columns, loc='upper left')
    # ax1.legend(cols)
    ax1.tick_params(axis='x', labelsize=11)
    ax1.tick_params(axis='y', labelsize=11)
    ax2.set_ylabel('인원 (천명)', fontsize=13)
    ax2.legend(['유치원아수', '초등학생수'], loc='lower left')
    fig.tight_layout()
    plt.show()


# def textMaker(cols):
#     if type(cols) == type([]):
#         text = ' / '.join(cols)
#         return text
#     else:
#         return cols