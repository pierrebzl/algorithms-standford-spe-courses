import random
import copy


def choose_random_edge(data):
    a = random.randint(0,len(data)-1)
    b = random.randint(1,len(data[a])-1)
    return a, b

def compute_nodes(data):
    data_head = []
    for i in range(len(data)):
        data_head.append(data[i][0])
    return data_head

def find_index(data_head,data,u,v):
    index = data_head.index(data[u][v])
    return index

def replace(data_head,data,index,u):
    for i in data[index][1:]:
        index_index = data_head.index(i)
    for position,value in enumerate(data[index_index]):
        if value == data[index][0]:
            data[index_index][position] = data[u][0]
    return data

def merge(data):
    u, v = choose_random_edge(data)
    data_head = compute_nodes(data)
    index = find_index(data_head,data,u,v)
    data[u].extend(data[index][1:])
    data = replace(data_head,data,index,u)
    data[u][1:] = [x for x in data[u][1:] if x!=data[u][0]]
    data.remove(data[index])
    return data

def karger_min_cut(data):
    data = copy.deepcopy(data)
    while len(data) > 2:
        data = merge(data)
    num = len(data[0][1:])
    return num

def calc_number(data,iteration):
    list = []
    for i in range(iteration):
        list.append(karger_min_cut(data))
    return min(list)

with open('./content/karger_min.txt') as f:
    data_set = []
    for ln in f:
        line = ln.split()
    if line:
        a = [int(x) for x in line]
    data_set.append(a)

print(calc_number(data_set, 200))
