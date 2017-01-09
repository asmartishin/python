import re

def abbreviate(s):
    words = re.findall('\w+', s)
    for word in words:
        if len(word) >= 4:
            s = s.replace(word, ''.join([str(word[0]), str(len(word[1:-1])), str(word[-1])]))
    return s

print(abbreviate('balloon; sits-cat-cat. monolithic: double-barreled; balloon, is.'))