import warnings


class Vertex:
    @classmethod
    def _all(container):
        def isVertex(object):
            if type(object) is not Vertex:
                raise TypeError(f"{type(object)} is not a Vertex")
            return True

        if type(container) is dict:
            container = container.values

        map(isVertex , container)
        return True

    def __init__(self, name, attributes=None, edges=None):
        self.name = name
        self.attributes = {}
        self.edges = {}

        if type(attributes) is dict:
            self.attributes = attributes
        
        if edges and Vertex._all(edges):
            if type(edges) is dict:
                self.edges = edges
            else:
                self.edges = {vertex.name: vertex for vertex in edges}

    def __str__(self):
        return str(self.name)

    def __getitem__(self, key):
        return self.edges[key]

    def __setitem__(self, key, vertex):
        if type(vertex) is not Vertex:
            raise TypeError(f"{type(vertex)} is not a Vertex")
        self.edges[key] = vertex

    def __iadd__(self, object):
        if type(object) is Vertex:
            self.edges += [object]
    
    def __isub__(self, object):
        if type(object) is Vertex:
            del self.edges[object.name]

    def __delitem__(self, key):
        del self.edges[key]

    def append(self, vertex):
        if type(vertex) is not Vertex:
            raise TypeError(f"{type(vertex)} is not a Vertex")
        if vertex.name in self.edges:
            raise ValueError(f"{vertex} is already and edge of {self}")

        self.edges[vertex.name] = vertex

    def __init__(self):
        pass