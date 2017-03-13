#!/usr/bin/env python


def rotate(state, pipe_numbers):
    pipe_numbers = set(pipe_numbers)
    result = []
    for i in range(len(state)):
        rotation_valid = True
        rotated_state = state[-i:] + state[:-i]
        for j in pipe_numbers:
            if rotated_state[j] != 1:
                rotation_valid = False
                break
        if rotation_valid:
            result.append(i)
    return result

if __name__ == '__main__':
    print(rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]))
