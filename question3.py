def question3(G):
# Kruskal's algorithm is implemented    
    vertices = G.keys()

    if len(vertices) <= 1:
        return "Error: Not enough data in Graph"
    # Then we need to get a set containing all of our edges
    """
    edges = set()
    for vertex in vertices:
        for connect in G[vertex]:
            if connect != vertex:
                edges.add((connect[1], connect[0], vertex))

    print edges
    
    # Output: {(2, 'A', 'B'), (2, 'B', 'A'), (5, 'B', 'C'), (5, 'C', 'B')}
    # As the graph G is undirected, (2, 'A', 'B') is the same as (2, 'B', 'A')
    # then edges is updated using the following code so that there is no duplicate edges
    """
    edges = set()
    for vertex in vertices:
        for connect in G[vertex]:
            if connect[0] < vertex:
                edges.add((connect[1], connect[0], vertex))
            elif connect[0] > vertex:
                edges.add((connect[1], vertex, connect[0]))

    # To implement Kruskal's algorithm, I will sort edges first, ascending in edge weight
    edges_sorted = sorted(edges)

    # The set edges_selected is used to store sets of (edge_weight, vertex_1, vertex_2)
    edges_selected = set()
    
    # For the next part of the code, we want to select edges and combine their vertice not all in one set
    # connected vertices are stored in a set, here is one example,
    # [set(['A', 'B', 'D', 'F']), set(['C', 'E']), set(['G'])]
    # ABDF is connected and CE is connected, G is not connected with any other connections
    # First, we update vertices to a list of sets
    vertices = [set(vertex) for vertex in vertices]

    # Then for each edge, we will compare its two vertices, and always combine the latter vertex into
    # a front set, for example, if our vertices is [set(['A']), set(['C']), set(['B']), set(['D']), set(['E'])]
    # and the current edge is (5, 'A', 'D'), then we will combine set(['A']) and set(['D']) into set(['A','D'])
    # which means we union these two sets and pop set(['D']). If the current edge is (5, 'C', 'E'), 
    # then we will combine set(['C']) and set(['E']) into set(['C','E']), of course, we will pop set(['E'])
    for edge in edges_sorted:
        for k in range(len(vertices)):
            if edge[1] in vertices[k]:
                node1_index = k
            if edge[2] in vertices[k]:
                node2_index = k
        
        if node1_index < node2_index:
            vertices[node1_index] = set.union(vertices[node1_index], vertices[node2_index])
            vertices.pop(node2_index)       
            edges_selected.add(edge)
        if node1_index > node2_index:
            vertices[node1_index] = set.union(vertices[node1_index], vertices[node2_index])
            vertices.pop(node1_index)       
            edges_selected.add(edge)
        
        # When all vertices are in one set, then all vertices are connected
        if len(vertices) == 1:
            break

    # Now we have all vertices and edges used for tranverse, the next step is to store them in a dictionary
    MST = {}
    for vertex in G.keys():
        MST[vertex] = []

    for edge in edges_selected:
        for vertex in MST.keys():
            if vertex == edge[1]:
                MST[vertex].append((edge[2],edge[0]))
            if vertex == edge[2]:
                MST[vertex].append((edge[1],edge[0]))

    return MST


####### Test Cases ######
G1 = {}
"""
shoule be: 
    Error: Not enough data in Graph
"""
G2 = {'A': [('B',2),('C',1),('D',4)], 
     'B': [('A',2), ('C',5)], 
     'C': [('A',1),('B',5),('D',3)],
     'D': [('A',4),('C',3)]}
question3(G2)
"""
shoule be:
    {'A': [('C', 1), ('B', 2)],
     'B': [('A', 2)],
     'C': [('A', 1), ('D', 3)],
     'D': [('C', 3)]}
"""

G3 = {'A':[('B',7),('D',5)],
  'B':[('A',7),('D',9),('C',8),('E',7)],
  'C':[('B',8),('E',5)],
  'D':[('A',5),('B',9),('E',15),('F',6)],
  'E':[('C',5),('B',7),('D',15),('F',8),('G',9)],
  'F':[('D',6),('E',8),('G',11)],
  'G':[('E',9),('F',11)]}
question3(G3)
"""
shoule be:
    {'A': [('D', 5), ('B', 7)],
     'B': [('E', 7), ('A', 7)],
     'C': [('E', 5)],
     'D': [('A', 5), ('F', 6)],
     'E': [('B', 7), ('G', 9), ('C', 5)],
     'F': [('D', 6)],
     'G': [('E', 9)]}
"""