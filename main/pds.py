
import sqlite3
import pandas as pd
import pymysql.cursors

from .models import mainTB
from .models import resultTB
# 데이터를 읽어서 1~31일 지출 금액 합 값을 리스트에 저장하자. list[31]
# db파일 경로 받아서 장고 모델에 저장하는 메소드 만들어야 함.
def test_func(path):

    # URL 변환
    path = path.replace("12","/")
    path = path.replace("34",":")
    path = path.replace("56","\\")

    conn = sqlite3.connect(path)
    conn1 = pymysql.connect(
        host="sudal-ins.c6gmxfp40ais.ap-northeast-2.rds.amazonaws.com",
        port=3306,
        user='admin',
        password='goekfsla12!',
        database='main_sc',
        charset='utf8'
    )

    query = "select * from mainTB"

    # df = pd.read_sql_query(query, conn)
    # ss = []
    # for i in range(len(df)):
    #     ss.append((df['ID'][i], df['DATE'][i], df['ca1'][i], df['ca2'][i], df['ca3'][i], df['ca4'][i], df['caption'][i]))
    #     # Table.objects.create(id=ss[i][0], DATE=ss[i][1], ca1 = ss[i][2], ca2 = ss[i][3], ca3 = ss[i][4], ca4 = ss[i][5], caption = ss[i][6])
    #
    # # result = df[df['ID'] >0]
    result=[]
    # name = ['ca1','ca2','ca3','ca4']
    # for i in range(0,4):
    #     result.append( df[name[i]].sum())
    #
    # # Result.objects.create(id=1,sum1=result[0],sum2=result[1],sum3=result[2],sum4=result[3])
    # tmp = {'ca1':result}
    # # print(tmp)
    #
    # # conn.close
    # # return df.to_dict('list')


    df = pd.read_sql_query(query,conn1 )
    name = ['ca1', 'ca2', 'ca3', 'ca4']
    for i in range(0,4):
        result.append( df[name[i]].sum())
    sql = "insert into resultTB(sum1,sum2,sum3,sum4) values(%s,%s,%s,%s)"
    val = (result[0],result[1],result[2],result[3])
    conn1.cursor().execute(sql,val)


    conn1.commit()
    conn.close
    conn1.close()


# test_func("C3456Users56lleel56Desktop56test.db")

def delete_data():
    conn = pymysql.connect(
        host="sudal-ins.c6gmxfp40ais.ap-northeast-2.rds.amazonaws.com",
        port=3306,
        user='admin',
        password='goekfsla12!',
        database='main_sc',
        charset='utf8'
    )
    sql = "delete from mainTB"
    sql1 = "delete from resultTB"
    conn.cursor().execute(sql)
    conn.cursor().execute(sql1)
    conn.commit()

    conn.close()
