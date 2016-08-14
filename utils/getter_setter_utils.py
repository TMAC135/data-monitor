# -*- coding:utf-8 -*-
'''
Author: Ran Tian
Created: 16/8/14
Version: 1.0
Update:
    08/16: show getter and setter method, convinient to generate
        properties for priviate fileds
'''

def show_getter_setter_method(input_object):
    '''
    Show the getter and setter for the field starting with
    _, which indicating it's private.
    :param input_object: The object with private field
    :return: The string representation for getter and setter
    :Example:

    '''
    template = '''
@property
def {key}(self):
    return self._{key}

@{key}.setter
def {key}(self, value):
    self._{key} = value
'''
    ret = []
    for key in input_object.__dict__:
        # exclude the logger filed
        if "logger" in key: continue
        # exclude the filed starting with __
        if key.startswith('_' + type(input_object).__name__):continue
        input_key = key
        if "_" == key[0]:
            input_key = key[1:]
        ret.append( template.format(key=input_key))
    return  "\n".join(ret)


if __name__ == '__main__':
    class Test(object):
        def __init__(self):
            self._v1 = 1
            self.__v2 = 2
            self._v3 = 3
    t = Test()
    print show_getter_setter_method(t)