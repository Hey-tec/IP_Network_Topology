# -*- coding = utf-8 -*-
# @Time : 2020/7/17 12:54
# @Author: Lucky_Pey
# @File : node_addr.py

# .......程序说明........

# .......调用模块.........
import sqlite3
import requests,re
# ........主函数..........

Node_Addr_Link = re.compile(r'.*"addr":"(.*)"},"msg":""}')
Hops_Link = re.compile(r'[(](.*?)[)]')

def IP2addr(IPV6):
    url = 'http://www.ipqi.co/config.php?callback=ipQuery.Callback&ip=' + IPV6.replace(':', '%3A') + '&source=ip2location&_='
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 83.0.4103.116Safari / 537.36"
    }

    Node_IPV6 = requests.get(url=url, headers=headers).text
    with open('./test_file/Node_IPV6.html','w',encoding='utf-8') as f:
        f.write(Node_IPV6)
    #print(re.findall(Node_Addr_Link,Node_IPV6))
    return ''.join(re.findall(Node_Addr_Link,Node_IPV6))

def GET_data():
    conn = sqlite3.connect('./test_file/probe_data.db')
    c = conn.cursor()
    #print("Opened database successfully")

    fp = open('./test_file/node_addr.txt','a',encoding='utf-8')
    Addr_data = []
    cursor = c.execute("SELECT id, src_address, dst_address, hops_num, hops from probe_data_20200701")
    rows = cursor.fetchall()

    for row in rows[90:96]:
        Each_Addr_data = []
        #print("ID = ", row[0])
        #print("Traceroute source address: ", row[1], type(row[1]))
        #print("Tracer]: ", row[2], type(row[2]))
        #print("Number of hops: ", row[3], type(row[3]))
        #print("Each Hops:", row[4], type(row[4]), "\n")
        #print(re.findall(Hops_Link,row[4]),type(re.findall(Hops_Link,row[4])))
        Each_Addr_data.append(IP2addr(row[1]))
        for Hop in re.findall(Hops_Link, row[4]):
            Each_Addr_data.append(IP2addr(Hop))
        Each_Addr_data.append(IP2addr(row[2]))
        #print(Each_Addr_data)
        fp.write(str(Each_Addr_data))
        fp.write('\n')
        print(row[0], "地址转换完成~")
    Addr_data.append(Each_Addr_data)

    print("Operation done successfully")
    conn.close()


if __name__ == "__main__":
    print("请开始你的表演...")
    GET_data()
    #IP2addr('2001:504:f::2f')

    print("完成！！！")