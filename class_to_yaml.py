#!/usr/bin/env python

from collections import OrderedDict, namedtuple
from functools import partial

import yaml
import yamlordereddictloader


Parents = namedtuple('Parents', ('mom', 'dad'))

class User(object):
    def __init__(self, name, age, parents):
        self.name = name
        self.age = age
        self.parents = parents

    def __str__(self):
        return "User({}, {}, {})".format(self.name, self.age, self.parents)


    def __repr__(self):
        return str(self)


class Always21User(User):
    def __init__(self, name, parents):
        super(Always21User, self).__init__(name, 21, parents)


def represent_ordereddict(dumper, tag, data):
    value = []

    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)

        value.append((node_key, node_value))

    return yaml.nodes.MappingNode(tag, value)


def yaml_class_representer(tag, fields, dumper, obj):
    return represent_ordereddict(dumper, tag, OrderedDict((x, getattr(obj, x, None)) for x in fields))


def yaml_class_constructor(klass, loader, node):
    value = loader.construct_mapping(node)
    return klass(**value)


if __name__ == '__main__':
    data = OrderedDict([
        ('users', [Always21User('Alex', None), Always21User('Anna', Parents('Olga', 'vadim'))]),
    ])

    data = yaml.dump(data, Dumper=yamlordereddictloader.Dumper, default_flow_style=False)
    print yaml.load(data, Loader=yamlordereddictloader.Loader)['users']

yaml.add_constructor(u'!user', partial(yaml_class_constructor, User))
yaml.add_constructor(u'!parents', partial(yaml_class_constructor, Parents))
yaml.add_representer(User, partial(yaml_class_representer, '!user', ['name', 'age', 'parents']))
yaml.add_representer(Parents,  partial(yaml_class_representer, '!parents', ['mom', 'dad']))


