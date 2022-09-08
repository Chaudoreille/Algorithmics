from collections import deque
from xml.dom import NotFoundErr


class Graph:
    def __init__(self):
        self.vertexes = {}
    
    def __getitem__(self, key):
        return self.vertexes[key]["value"]

    def __setitem__(self, key, value):
        vertex = self.vertexes.get(key, {"edges": []})
        vertex["value"] = value
        self.vertexes.update(key, vertex)
 
        return self

    def __delitem__(self, key):
        if key in self.vertexes:
            for neighbor in self.vertexes[key]["edges"]:
                try:
                    self.vertexes[neighbor]["edges"].remove(key)
                except(ValueError):
                    pass

        return self

    def add_vertex(self, vertex, value, edges):
        self.vertexes.update({
            vertex: {
                "value": value,
                "edges": edges
            }
        })
        for neighbor_id in edges:
            neighbor = self.vertexes.get(neighbor_id, {"value": None, "edges":[]})
            neighbor["edges"].append(id)
            self.vertexes.update({neighbor_id: neighbor})

        return self

    def add_edge(self, id_vertex_1, id_vertex_2):
        if id_vertex_1 not in self.vertexes:
            raise ValueError(f"{id_vertex_1} is not a vertex in the graph")
        if id_vertex_2 not in self.vertexes:
            raise ValueError(f"{id_vertex_2} is not a vertex in the graph")
 
        self.vertexes[id_vertex_1]["edges"].append(id_vertex_2)
        self.vertexes[id_vertex_2]["edges"].append(id_vertex_1)

        return self

    def bfs(self, start, needle):
        queue = deque()

        if start not in self.vertexes:
            raise ValueError("There is no vertex labeled {}".format(start))

        queue.append(start)

        while len(queue):
            cursor = queue.popleft()

            if cursor == needle:
                return self.vertexes[cursor]["value"]
            for vertex in self.vertexes[cursor["edges"]]:
                queue.append(vertex)

        raise NotFoundErr("Vertex {} not in graph".format(needle))

    def dfs(self, start, value):
        pass