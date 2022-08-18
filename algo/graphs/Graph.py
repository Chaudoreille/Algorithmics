class Graph:
    def __init__(self):
        self.vertexes = {}
    
    def __getitem__(self, key):
        return self.vertexes[key]["value"]

    def __setitem__(self, key, value):
        vertex = self.vertexes.get(key, {"neighbors": []})
        vertex["value"] = value
        self.vertexes.update(key, vertex)
 
        return self

    def __delitem__(self, key):
        if key in self.vertexes:
            for neighbor in self.vertexes[key]["neighbors"]:
                try:
                    self.vertexes[neighbor]["neihbors"].remove(key)
                except(ValueError):
                    pass

        return self



    def add_vertex(self, id, vertex, neighbors):
        self.vertexes[id] = self.vertexes.update(id, {
            "value": vertex,
            "neighbors": neighbors
        })
        for v in neighbors:
            self.vertexes.update(v, {
                "neighbors": self.vertexes.get(v, {"neighbors": []})["neighbors"].append(id)                
            })

    def add_edge(self, id_vertex_1, id_vertex_2):
        v1 = self.vertexes.get(id_vertex_1, {"neighbors": []})
        v2 = self.vertexes.get(id_vertex_2, {"neighbors": []})

        v1["neighbors"] += [id_vertex_2]
        v2["neighbors"] += [id_vertex_1]
 
        self.vertexes.update(id_vertex_1, v1)
        self.vertexes.update(id_vertex_2, v2)

    def bfs(self, start, value):
        pass

    def dfs(self, start, value):
        pass