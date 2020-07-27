# -*- coding = utf-8 -*-
# @Time : 2020/7/16 18:22
# @Author: Lucky_Pey
# @File : warts2list.py
# @Software : PyCharm

# .......调用模块.........
import warts
from warts.traceroute import Traceroute
import sqlite3
# ........主函数..........

def warts2list():
    datalist = []
    with open('./test_file/path_txt_using','r') as fp:
        for url in fp.readlines():
            data = []
            open_path = './20200701warts/' + url[79:-3]
            with open(open_path, 'rb') as f:
                record = warts.parse_record(f)
                while not isinstance(record, Traceroute):
                    record = warts.parse_record(f)
                if record.src_address:
                    print("Traceroute source address:", record.src_address)
                    data.append(record.src_address)
                if record.dst_address:
                    print("Traceroute destination address:", record.dst_address)
                    data.append(record.dst_address)
                print("Number of hops:", len(record.hops))
                print(record.hops)
                data.append(str(len(record.hops)))
                data.append(str(record.hops))
                datalist.append(data)
        print(datalist)
    return datalist



def init_DB(dbpath):
    sql = '''
        create table probe_data_20200701(
            id integer primary key autoincrement,
            src_address text,
            dst_address text,
            hops_num numeric,
            hops text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def SaveData2DB(datalist,dbpath):
    init_DB(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            #if index == 3:
                #continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into probe_data_20200701(
                src_address,dst_address,hops_num,hops)
                values(%s)'''%",".join(data)
        #print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    print("请开始你的表演...")
    dbpath = './test_file/probe_data.db'
    datalist = warts2list()
    SaveData2DB(datalist,dbpath)
    #warts2list()
    print("完成！！！")

