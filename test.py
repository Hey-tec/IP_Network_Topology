# -*- coding = utf-8 -*-
# @Time : 2020/7/16 20:55
# @Author: Lucky_Pey
# @File : test.py
# @Software : PyCharm

# .......调用模块.........
import gzip
import sqlite3 as db
import re
import numpy as np
# ........主函数..........

def readFronSqllite(db_path,exectCmd):
    conn = db.connect(db_path)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
    cursor=conn.cursor()        # 该例程创建一个 cursor，将在 Python 数据库编程中用到。
    conn.row_factory=db.Row     # 可访问列信息
    cursor.execute(exectCmd)    #该例程执行一个 SQL 语句
    rows=cursor.fetchall()      #该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
    return rows
    #print(rows[0][2]) # 选择某一列数据

def gz2warts():
    rows = readFronSqllite('./test_file/probe_data.db', "SELECT  hops_num from probe_data_20200701")
    num = [int(s) for s in re.findall(r'\b\d+\b', str(rows))]
    print(num,type(num))

if __name__ == "__main__":
    print("请开始你的表演...")
    #gz2warts()
    color_array = []
    for i in range(181):
        color_array.append('red')
    color_array[5] = 'green'
    print(color_array)


