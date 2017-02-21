#!/usr/bin/env python3

import math
import re

MATRIX_COLUMNS = ('A', 'D', 'F', 'G', 'V', 'X')


def keyword_uniq_letters(keyword):
    keyword_letters = set(keyword)
    result = ''
    for letter in keyword:
        if letter in keyword_letters:
            result += letter
            keyword_letters.remove(letter)
    return result


def encode(message, secret_alphabet, keyword):
    message = re.sub(r"[ :,'!-/?]", '', message).lower()
    keyword = keyword_uniq_letters(keyword)
    print(message)

    encoded_message = []
    for letter in message:
        letter_index = secret_alphabet.index(letter)
        encoded_message.extend((
            MATRIX_COLUMNS[letter_index // len(MATRIX_COLUMNS)],
            MATRIX_COLUMNS[letter_index % len(MATRIX_COLUMNS)]
        ))

    shift = 0
    keyword_matrix = []
    for y in range(len(message)):
        if y + shift >= len(encoded_message):
            break
        keyword_matrix.append([
            encoded_message[x + y + shift] if x + y + shift < len(encoded_message) else '' for x in range(len(keyword))
        ])
        shift += len(keyword) - 1

    keyword_letter_indices = {v: i for i, v in enumerate(keyword)}
    result = ''

    for letter in ''.join(sorted(keyword)):
        result += ''.join([keyword_matrix[x][keyword_letter_indices[letter]] for x in range(len(keyword_matrix))])
    return result


def decode(message, secret_alphabet, keyword):
    secret_alphabet_matrix = []
    secret_alphabet_matrix_letter_indices = {v: i for i, v in enumerate(MATRIX_COLUMNS)}
    shift = 0
    for y in range(len(MATRIX_COLUMNS)):
        secret_alphabet_matrix.append([secret_alphabet[x + y + shift] for x in range(len(MATRIX_COLUMNS))])
        shift += len(MATRIX_COLUMNS) - 1

    keyword = keyword_uniq_letters(keyword)
    message = list(message)

    keyword_matrix_size = math.ceil(len(message) / len(keyword))
    keyword_matrix_letter_count = {
        v: keyword_matrix_size if (i < (len(message) % len(keyword)) or len(message) % len(keyword) == 0) \
        else keyword_matrix_size - 1 for i, v in enumerate(keyword)
    }

    keyword_matrix_sorted = []
    for letter in ''.join(sorted(keyword)):
        if keyword_matrix_letter_count[letter] <= keyword_matrix_size - 1:
            keyword_matrix_sorted.append(message[:keyword_matrix_letter_count[letter]] + [''])
        else:
            keyword_matrix_sorted.append(message[:keyword_matrix_letter_count[letter]])
        message = message[keyword_matrix_letter_count[letter]:]

    keyword_sorted_letter_indices = {v: i for i, v in enumerate(sorted(keyword))}
    keyword_letter_indices = {v: i for i, v in enumerate(keyword)}
    keyword_matrix = [[None] * len(keyword) for y in range(keyword_matrix_size)]
    for letter in keyword:
        for y in range(keyword_matrix_size):
            keyword_matrix[y][keyword_letter_indices[letter]] = \
                    keyword_matrix_sorted[keyword_sorted_letter_indices[letter]][y]

    encoded_message = []
    for y in range(keyword_matrix_size):
        for x in range(len(keyword)):
            encoded_message.append(keyword_matrix[y][x])

    result = ''
    for letter_indices in [encoded_message[x:x + 2] for x in range(0, len(encoded_message), 2)]:
        if letter_indices[0] in MATRIX_COLUMNS and letter_indices[1] in MATRIX_COLUMNS:
            result += secret_alphabet_matrix[secret_alphabet_matrix_letter_indices[letter_indices[0]]]\
                    [secret_alphabet_matrix_letter_indices[letter_indices[1]]]
    return result


if __name__ == '__main__':
    print(encode("attack at 12:00 am", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz", "privacy"))
#    print(decode("VGFFAXDVAVXVXXGVXXFGVAFGV", "d9sr4qxvaz75yu2hkwpm8j63b1legot0ifnc", "monty"))
#    print(decode("FXGAFVXXAXDDDXGA", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g", "cipher"))
#    print(encode("One 1, Two 2, Three 3, Four 4, Five 5, Six 6, Seven 7, Eight 8, Nine 9, Zero 0", "d9sr4qxvaz75yu2hkwpm8j63b1legot0ifnc", "monty"))
