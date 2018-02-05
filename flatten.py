#!/usr/bin/env python


def flatten(data_set, data, current_key=None):
    is_dict = True if isinstance(data, dict) else False
    iterable = data.iteritems() if is_dict else enumerate(data)

    for key, value in iterable:
        if current_key:
            new_key = '{}/{}'.format(current_key, key) if is_dict else current_key
        else:
            new_key = key if is_dict else ''

        if isinstance(value, (dict, list)):
            flatten(data_set, value, new_key)
        else:
            data_set.add(u'{}/{}'.format(new_key, value))


def main():
    d = {'a': [{'b': 'e'}, {'g': 'r'}], 'c': {'t': 'f'}}
    s = set()
    flatten(s, d)

    for i in s:
        print i


if __name__ == '__main__':
    main()

