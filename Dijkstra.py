import time
from collections import defaultdict
from heapq import *

v_data = []
e_data = []
with open('v.txt','r')as fv:#importand file in YngdaFan.zip
    for line in fv.readlines():
        if '#' in line:
            continue
        element = (line.strip().split(','))
        v_data.append([int(element[0]),int(element[1])])
fv.close()
with open('e.txt','r')as fe:
    for line in fe.readlines():
        if '#' in line:
            continue
        element = (line.strip().split(','))
        e_data.append([int(element[0]),int(element[1]),int(element[2])])
fe.close()

G = defaultdict(list)
for Content in e_data:
    G[Content[0]].append((Content[2],Content[1]))
    G[Content[1]].append((Content[2],Content[0]))
              
def Dijkstra(start,end,graph):
    queue = [(0,start,())]
    click = set()
    dic = {start:0}
    count = 0
    while queue:
        (cost,v_one,path) = heappop(queue)
        if v_one in click:
            continue
        click.add(v_one)
        path += (v_one,)
        if v_one == end:
            return (cost,path,count)
        for m,v_two in graph.get(v_one,()):
            if v_two in click:
                continue
            if v_two not in dic or cost + m < dic[v_two]:
                dic[v_two] = cost + m
                heappush(queue, (cost + m, v_two, path))
                count += 1
    return "No way"

Source = 3
Destination = 99
print("The start vertex is:",Source)
print("The end vertex is:",Destination)

since = time.time()

result = Dijkstra(Source,Destination,G)
print("cost:",result[0])
print("path:",result[1])
print("steps:",result[2])
time_elapsed = time.time() - since

print("The time cost is: %.4f"%time_elapsed)
