from collections import deque
from multiprocessing.sharedctypes import Value
from typing import Type
from xml.dom import NotFoundErr

def vertex(container):
    if type(container) is dict:
        for key, value in container.items():
            match key:
                case "attributes":
                    if type(value) is not dict:
                        raise TypeError(f"{type(value)} is not a dictionary")
                case "edges":
                    if type(value) is not list:
                        raise TypeError(f"{type(value)} is not a list")
                case _:
                    raise KeyError(f"{key} should be one of 'attributes' or 'edges'")
        return container
    else:
        return {"edges": list(container)}

class Graph:
    def __init__(self, vertexes=None):
        if vertexes == None:
            vertexes = {}

        if type(vertexes) is dict:
            self.vertexes = vertexes
        else:
            raise TypeError(f"{type(vertexes)} is not a dictionary")

        for v in self.vertexes:
            self.vertexes.update({v: vertex(self.vertexes[v])})
    
    def __getitem__(self, key):
        return self.vertexes[key]["attributes"]

    def __setitem__(self, key, value):
        self.vertexes.update({key: vertex(value)})

        return self

    def __len__(self):
        return len(self.vertexes)

    def __str__(self):
        return str(self.vertexes)

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
        visited = set()

        if start not in self.vertexes:
            raise ValueError(f"There is no vertex labeled {start}")

        queue.append(start)

        while len(queue):
            cursor = queue.popleft()

            if cursor == needle:
                return cursor

            for neighbor in self.vertexes[cursor]["edges"]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
            visited.add(cursor)

        raise NotFoundErr(f"Vertex {needle} not in graph")

    def dfs(self, start, value):
        pass