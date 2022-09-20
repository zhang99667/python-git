import networkx as nx
import matplotlib.pyplot as plt

# 创建无向图 G
G = nx.Graph()
print(G.is_directed())

# 创建有向图 H
H = nx.DiGraph()
print(H.is_directed())

# 添加图属性
G.graph["Name"] = "Bar"
print(G.graph)

# 添加一个节点和属性
G.add_node(0, feature=5, label=0)

# 获取节点0的属性
node_0_attr = G.nodes[0]
print("Node 0 has the attributes {}".format(node_0_attr))

G.add_nodes_from([
  (1, {"feature": 1, "label": 1}),
  (2, {"feature": 2, "label": 2})
])
#(node, attrdict)
# 循环所有的节点
# 设置data=True 返回节点属性
for node in G.nodes(data = True):
    print(node)
# 得到节点数目
num_nodes = G.number_of_nodes()
print("G has {} nodes".format(num_nodes))

# 设置一条边到另一条边的权重为0.5
G.add_edge(0,1,weight=0.5)
# 对边(0,1)添加属性
edge_0_1_attr = G.edges[(0,1)]
print("Edge(0,1) has the attributes {}".format(edge_0_1_attr))

#  添加多条边和权重
G.add_edges_from([
    (1,2,{"weight":0.3}),
    (2,0,{"weight":0.1})
])
# 循环所有的边
# 如果没有设置data=True 因此只返回边
for edge in G.edges():
    print(edge)
# 获取节点的数目
num_edges = G.number_of_edges()
print("G has {} edges".format(num_edges))

# 画图
nx.draw(G,with_labels=True)
plt.savefig('pic.png',bbox_inches='tight')