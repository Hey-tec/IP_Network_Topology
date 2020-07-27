# -*- coding = utf-8 -*-
# @Time : 2020/7/18 13:14
# @Author: Lucky_Pey
# @File : IP_network.py

# .......程序说明........


# .......调用模块.........
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import re,sqlite3
import numpy as np
from operator import itemgetter
# ........主函数..........
plt.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False

conn = sqlite3.connect('./test_file/probe_data.db')
c = conn.cursor()
fp = open('./test_file/node_addr.txt','a',encoding='utf-8')
cursor = c.execute("SELECT hops_num from probe_data_20200701")
rows = cursor.fetchall()
num = [int(s) for s in re.findall(r'\b\d+\b', str(rows))]
num_num = 0

plt.subplots(1, 1, figsize=(15, 15))
G = nx.DiGraph()

fp = open('./test_file/node_addr.txt','r')
for line in fp.readlines():
        line_list = re.findall(re.compile(r"'(.*?)'"), str(line))
        G.add_nodes_from(line_list)
        for index in range(num[num_num]):
                if line_list[index] != line_list[index+1]:
                        G.add_edge(line_list[index], line_list[index+1])
        num_num = num_num + 1

size_array = np.ones(181)*300
color_array = []
for i in range(181):
        color_array.append('red')
# for name in sorted(G.nodes()):
#         print(name,sorted(G.nodes()).index(name))
for degree in G.degree():                             #遍历度分布
        for name in sorted(G.nodes()):
                if degree[1] == 3 and name == degree[0]:
                        size_array[sorted(G.nodes()).index(name)] = 400
                        color_array[sorted(G.nodes()).index(name)] = 'green'
                if degree[1] == 4 and name == degree[0]:
                        size_array[sorted(G.nodes()).index(name)] = 600
                        color_array[sorted(G.nodes()).index(name)] = 'green'
                if degree[1] == 5 and name == degree[0]:
                        size_array[sorted(G.nodes()).index(name)] = 800
                        color_array[sorted(G.nodes()).index(name)] = 'green'
                if degree[1] > 6 and degree[1]<15 and name == degree[0]:
                        size_array[sorted(G.nodes()).index(name)] = 1000
                        color_array[sorted(G.nodes()).index(name)] = 'red'
                if degree[1] >= 15 and name == degree[0]:
                        size_array[sorted(G.nodes()).index(name)] = 1200
                        color_array[sorted(G.nodes()).index(name)] = 'red'
                if degree[1] >= 0 and degree[1] < 3 and name == degree[0]:
                        size_array[sorted(G.nodes()).index(name)] = 300
                        color_array[sorted(G.nodes()).index(name)] = 'blue'
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
dmax = max(degree_sequence)
plt.plot(degree_sequence, "b-", marker="o")

plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")
plt.axes([0.9, 0.1, 0.78, 0.78])

nx.draw_spring(G, nodelist=sorted(G.nodes()), width=2, node_size=size_array,node_color=color_array,font_weight='bold',with_labels=False,style='dotted',cmap=plt.cm.Blues)
print(size_array)
print(color_array)
# for k,v in nx.out_degree_centrality(G).items():        #遍历中心度
#         print(k,v)
#         if v >0.03 :
#                 G.add_node(str(k),node_size=800,color='red')


plt.title('IP Network')
plt.axis('on')
plt.xticks([])
plt.yticks([])
plt.savefig('./network_picture/IP_network_0701.png',bbox_inches='tight')



