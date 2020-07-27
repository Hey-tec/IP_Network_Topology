# -*- coding = utf-8 -*-
# @Time : 2020/7/16 18:29
# @Author: Lucky_Pey
# @File : Download_warts.py
# @Software : PyCharm

# .......调用模块.........
import requests,re
import gzip,os
# ........主函数..........
Download_Link = re.compile(r'<a href=".*">(.*)</a>')

def Get_warts_url():
    probe_data_url = 'http://data.caida.org/datasets/topology/ark/ipv6/probe-data/2020/07/'
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 83.0.4103.116Safari / 537.36"
    }
    probe_data_html = requests.get(url= probe_data_url,headers=headers).text
    with open('./test_file/probe_data.html','w',encoding='utf-8') as f:
        f.write(probe_data_html)
    Download_p = re.findall(Download_Link,probe_data_html)
    path = []
    path_txt = open('./test_file/path_txt.txt','w',encoding='utf-8')
    for i in Download_p:
        Download_path = probe_data_url + i
        path_txt.write(Download_path + '\n')
        path.append(Download_path)
    print(path[2])
    return path

def Download_warts_file():
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 83.0.4103.116Safari / 537.36"
    }
    with open('./test_file/path_txt_using','r') as f:
        for url in f.readlines():
            url = url.strip('\n')
            probe_d = requests.get(url=url, headers=headers).content
            warts_file = open('./20200701gz/'+ url[79:], 'wb')
            warts_file.write(probe_d)
            print(url[79:] , "下载成功！")

def gz2warts():
    with open('./test_file/path_txt_using','r') as f:
        for url in f.readlines():
            url = url.strip('\n')
            file_name = './20200701gz/' + url[79:]
            f_name = file_name.replace(".gz", "")
            f_name = f_name.replace("20200701gz", "20200701warts")
            print(f_name)
            g_file = gzip.GzipFile(file_name)           #创建gzip对象
            open(f_name, "wb+").write(g_file.read())     #gzip对象用read()打开后，写入open()建立的文件里。
        g_file.close()                           #关闭gzip对象

if __name__ == "__main__":
    print("请开始你的表演...")
    #Download_warts_file()
    gz2warts()
    print("爬取完成！！！")

