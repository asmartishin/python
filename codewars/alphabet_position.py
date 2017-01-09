def alphabet_position(text):
    string_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    string_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_dict  = {}
    new_text = []
    for i in xrange(len(string_lowercase)):
        alphabet_dict[string_lowercase[i]] = i + 1
        alphabet_dict[string_uppercase[i]] = i + 1
    for i in text:
        if i in alphabet_dict:
            i = alphabet_dict[i]
            new_text.append(i)
    return ' '.join(map(str, new_text))

text = "The sunset sets at twelve o' clock."
print(alphabet_position(text))