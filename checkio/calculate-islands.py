#!/usr/bin/env python

def island(land_map, x, y, areas):
    lengthX = len(land_map)
    lengthY = len(land_map[0])
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (0 <= x + i < lengthX) and (0 <= y + j < lengthY):
                if land_map[x + i][y + j] == 1:
                    land_map[x + i][y + j] = '*'
                    areas[-1] += 1
                    island(land_map, x + i, y + j, areas)

def checkio(land_map):
    areas = []

    for x, row in enumerate(land_map):
        for y, el in enumerate(row):
            if el == 1:
                land_map[x][y] = '*'
                areas.append(1)
                island(land_map, x, y, areas)
    areas.sort()
    return areas

if __name__ == '__main__':
    print(checkio(
        [[0,0,0,0,0],[0,0,1,1,0],[0,0,0,1,0],[0,1,1,0,0]]
    	    ))
