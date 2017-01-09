def rgb(r, g, b):
    dec_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                  12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    a = []
    for i in (r,g,b):
        if i > 255:
            i = 255
        elif i < 0:
            i = 0
        if i == 0:
            a.append('00')
        elif i < 16 :
            a.append('0')
            a.append(dec_to_hex[i % 16])
        else:
            while i > 0:
                a.append(dec_to_hex[i % 16])
                i /= 16
            a[-1], a[-2] = a[-2], a[-1]
    print ''.join(i for i in a)

rgb(254, 253, 252)



