# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from functools import partial
from collections import OrderedDict

import yaml


def represent_ordereddict(dumper, tag, data):
    value = []

    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)

        value.append((node_key, node_value))

    return yaml.nodes.MappingNode(tag, value)


class ClassDumper(object):
    __metaclass__ = ABCMeta

    def __init__(self, klass, tag, representer, constructor):
        self._class = klass
        self._tag = tag
        self._representer = representer
        self._constructor = constructor

    @abstractmethod
    def add_representer(self):
        raise NotImplementedError

    @abstractmethod
    def add_constructor(self):
        raise NotImplementedError


class ClassDumperString(ClassDumper):
    def __init__(self, klass, tag):
        self._fields = ()
        super(ClassDumperString, self).__init__(
            klass,
            tag,
            self.yaml_str_class_representer,
            self.yaml_str_class_constructor,
        )

    @staticmethod
    def yaml_str_class_representer(tag, dumper, obj):
        return dumper.represent_scalar(tag, str(obj))

    @staticmethod
    def yaml_str_class_constructor(klass, loader, node):
        data = loader.construct_scalar(node)
        return klass(data)

    def add_representer(self):
        return yaml.add_representer(
            self._class,
            partial(
                self._representer,
                self._tag,
            )
        )

    def add_constructor(self):
        return yaml.add_constructor(
            self._tag,
            partial(
                self._constructor,
                self._class,
            )
        )


class ClassDumperOrderedDict(ClassDumper):
    def __init__(self, klass, tag, fields):
        self._fields = fields
        super(ClassDumperOrderedDict, self).__init__(
            klass,
            tag,
            self.yaml_ordereddict_class_representer,
            self.yaml_ordereddict_class_constructor,
        )

    @staticmethod
    def yaml_ordereddict_class_representer(tag, fields, dumper, obj):
        return represent_ordereddict(dumper, tag, OrderedDict((x, getattr(obj, x, None)) for x in fields))

    @staticmethod
    def yaml_ordereddict_class_constructor(klass, loader, node):
        data = loader.construct_mapping(node)
        return klass(**data)

    def add_representer(self):
        yaml.add_representer(
            self._class,
            partial(
                self._representer,
                self._tag,
                self._fields,
            )
        )

    def add_constructor(self):
        yaml.add_constructor(
            self._tag,
            partial(
                self._constructor,
                self._class,
            )
        )
