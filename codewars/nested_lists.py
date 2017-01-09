def list_depth(l):
    count = 1
    add = [0]
    for i in l:
        if isinstance(i, list):
            add.append(list_depth(i))
    return count + max(add)

print(list_depth([[[]],[], []]))
