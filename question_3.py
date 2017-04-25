def question3(g):
    # Make sure g is a dictionary
    if not isinstance(g, dict):
        return "Error: G is not dictionary"

    # Make sure g has more than one node
    if len(g) < 2:
        return "Error: G has not enough vertices to form edges"

    # Get a set of vertices
    vertices = g.keys()

    # Get unique set of edges
    edges = set()
    for i in vertices:
        for j in g[i]:
            if i > j[0]:
                edges.add((j[1], j[0], i))
            elif i < j[0]:
                edges.add((j[1], i, j[0]))

    # Sort edges by weight
    edges = sorted(list(edges))

    # Loop through edges and store only the needed ones
    output_edges = []
    vertices = [set(i) for i in vertices]
    for i in edges:
        # Get indices of both vertices
        for j in xrange(len(vertices)):
            if i[1] in vertices[j]:
                i1 = j
            if i[2] in vertices[j]:
                i2 = j

        # Store union in the smaller index and pop the larger index
        # Also store the edge in output_edges
        if i1 < i2:
            vertices[i1] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i2)
            output_edges.append(i)
        if i1 > i2:
            vertices[i2] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i1)
            output_edges.append(i)

        # Terminate early when all vertices are in one graph
        if len(vertices) == 1:
            break

    # Generate the output graph from output_edges
    output_graph = {}
    for i in output_edges:
        if i[1] in output_graph:
            output_graph[i[1]].append((i[2], i[0]))
        else:
            output_graph[i[1]] = [(i[2], i[0])]

        if i[2] in output_graph:
            output_graph[i[2]].append((i[1], i[0]))
        else:
            output_graph[i[2]] = [(i[1], i[0])]
    return output_graph


"""
Test Cases

G = {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)],
     'C': [('B', 5)]}

print question3(G) -> {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}
print question3(123) -> Error: g is not a dictionary
print question3({})  -> Error: g has not enough vertices to form edges
"""
