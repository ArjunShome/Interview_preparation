
# def dijkstrasAlgorithm(start, edges):
#     tot_vertices = len(edges)
#     # Write your code here.
#     edgeMinDistance = [float('inf')] * len(edges)
#     edgeMinDistance[start] = 0

#     visited = set()

#     while len(visited) != tot_vertices:
#         vertex, cur_distance = getVertexWithMinDistance(edgeMinDistance, visited)

#         if cur_distance == float('inf'):
#             break

#         visited.add(vertex)

#         for edge in edges[vertex]:
#             destination, distanceToDestination = edge

#             if destination in visited:
#                 continue

#             newPathDistance = cur_distance + distanceToDestination
#             current_dest_distance = edgeMinDistance[destination]
#             if newPathDistance < current_dest_distance:
#                 edgeMinDistance[destination] = newPathDistance

#     return list(map(lambda x: -1 if x == float('inf') else x, edgeMinDistance))

# def getVertexWithMinDistance(edgeMinDistance, visited):
#     currentMinDistance = float('inf')
#     vertex = None

#     for vertexID, distance in enumerate(edgeMinDistance):
#         if vertexID in visited:
#             continue
#         if distance <= currentMinDistance:
#             vertex = vertexID
#             currentMinDistance = distance
#     return vertex, currentMinDistance





def dijkstrasAlgorithm(start, edges):
    total_vertex = len(edges)
    min_vertex_distance = [float('inf')] * total_vertex
    min_vertex_distance[start] = 0
    vertex_seen = set()

    while len(vertex_seen) != total_vertex:
        cur_vertex, cur_distance = get_min_vertex_distance(min_vertex_distance, vertex_seen)

        if cur_distance == float('inf'):
            break  # no edges exist or empty list of edges
        
        vertex_edges = edges[cur_vertex]
        vertex_seen.add(cur_vertex)

        for edge in vertex_edges:
            dest_vertex = edge[0]
            dest_vertex_distance = edge[1] + cur_distance
            
            if dest_vertex in vertex_seen:
                continue
            cur_dest_vertex_distance = min_vertex_distance[dest_vertex]
            if dest_vertex_distance < cur_dest_vertex_distance:
                min_vertex_distance[dest_vertex] = dest_vertex_distance

    for vertex_idx in range(len(min_vertex_distance)):
        if min_vertex_distance[vertex_idx] == float('inf'):
            min_vertex_distance[vertex_idx] = -1

    return min_vertex_distance


def get_min_vertex_distance(min_vertex_distance, vertex_seen):
    distance = float('inf')
    vertex = None

    for vertex_idx, cur_distance in enumerate(min_vertex_distance):
        if vertex_idx in vertex_seen:
            continue
        if cur_distance < distance:
            distance = cur_distance
            vertex = vertex_idx
    return vertex, distance

if __name__ == '__main__':
    start = 0
    edges = [
        [[1,7]],
        [[2,6], [3,20], [4,3]],
        [[3,14]],
        [[4,2]],
        [],
        [],
    ]
    print(dijkstrasAlgorithm(start, edges))