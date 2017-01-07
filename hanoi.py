#!/usr/bin/env python


class Stack(object):
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, value):
        self.items.append(value)

    def is_empty(self):
        return not bool(len(self.items))

    def __str__(self):
        return ', '.join(str(x) for x in self.items) if self.items else 'Empty'

    def __repr__(self):
        return self.__str__()


class Tower(object):
    def __init__(self, rings_num):
        self.rods = ['A', 'B', 'C']
        self.data = {rod: Stack() for rod in self.rods}
        self.rings = list(xrange(1, rings_num + 1))[::-1]
        for ring in self.rings:
            self.data[self.rods[0]].push(ring)

    def move_ring(self, first_rod, second_rod):
        self.data[second_rod].push(self.data[first_rod].pop())

    def __str__(self):
        return str(self.data)


def solution(count, tower, source, target, buf):
    if count > 0:
        solution(count - 1, tower, source, buf, target)
        tower.move_ring(source, target)
        print(tower)
        solution(count -1, tower, buf, target, source)


if __name__ == '__main__':
    tower = Tower(5)
    solution(5, tower, 'A', 'B', 'C')
