#!/usr/bin/env python


class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.connections = set()

    def add_connection(self, key):
        self.connections.add(key)

    def connections(self):
        return self.connections

    def key(self):
        return self.key

    def __str__(self):
        return '{} -> {}'.format(self.key, str([x for x in self.connections]))

    def __repr__(self):
        return self.__str__()


class Graph(object):
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vertices.get(key)

    def vertices(self):
        return self.vertices.keys()

    def add_edge(self, first_vertex,  second_vertex):
        if first_vertex not in self.vertices:
            self.add_vertex(first_vertex)
        if second_vertex not in self.vertices:
            self.add_vertex(second_vertex)
        self.vertices[first_vertex].add_connection(second_vertex)
        self.vertices[second_vertex].add_connection(first_vertex)

    def __contains__(self, key):
        return key in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def __getitem__(self, key):
        return self.get_vertex(key)

    def __str__(self):
        return str([v for v in self.vertices.values()])

    def __repr__(self):
        return self.__str__()


def  power_supply_helper(curr_vertex):
    while CITIES_POWER[curr_vertex]['power'] > CITIES_POWER[curr_vertex]['limit']:
        for conn_vertex in POWER_GRAPH[curr_vertex].connections:
            CITIES_POWER[conn_vertex]['power'] += 1
        CITIES_POWER[curr_vertex]['power'] -= 1

    CITIES_POWER[curr_vertex]['processed'] = True

    for conn_vertex in POWER_GRAPH[curr_vertex].connections:
        if CITIES_POWER[conn_vertex]['power'] > CITIES_POWER[conn_vertex]['limit'] and not CITIES_POWER[conn_vertex]['processed']:
            power_supply_helper(conn_vertex)


def power_supply(network, power_plants):
    global POWER_GRAPH
    global CITIES_POWER

    POWER_GRAPH = Graph()
    CITIES_POWER = {}

    result = set()
    for connection in network:
        CITIES_POWER.update({x: {'power' : 0, 'processed': False, 'limit': 1} if x not in power_plants else {
            'power' : power_plants[x], 'processed': False, 'limit': 0} for x in connection})
        POWER_GRAPH.add_edge(*(connection))
    for power_plant in power_plants:
        power_supply_helper(power_plant)
    for k, v in CITIES_POWER.iteritems():
        if v['power'] < v['limit']:
            result.add(k)
    return result


if __name__ == '__main__':
    print(power_supply([["p1","c1"],["c1","c2"],["c2","c3"]],{"p1":3}))

