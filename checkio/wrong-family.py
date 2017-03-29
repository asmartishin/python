#!/usr/bin/env python


def is_family(tree):
    family = set(tree[0])
    for father, son in tree[1:]:
        if father in family and son not in family:
            family.add(son)
        else:
            return False
    return True


if __name__ == '__main__':
    print(is_family([['Logan', 'Mike'], ['Logan', 'Jack'], ['Mike', 'Alexander']]))

