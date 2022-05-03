import re;
from itertools import repeat;
import copy;
from collections import OrderedDict

def funcTemplateGenerator(template, comps):
    def funcTemplate(*args, **kwargs):
        nonlocal template
        nonlocal comps
        templateCopy = copy.deepcopy(template)
        compsCopy = copy.deepcopy(comps)
        if (len(args) > 0):
            i = 0
            while(i < len(args)):
                assert isinstance(args[i], str)
                key = compsCopy.popitem()
                templateCopy = templateCopy.replace("{{" + key[0] + "}}", args[i])
                i+=1
        for value in kwargs.keys():
            assert isinstance(kwargs[value], str)
            compsCopy.pop(value)
            templateCopy = templateCopy.replace("{{" + value + "}}", kwargs[value])

        if (len(compsCopy) == 0):
            return templateCopy
        else:
            return funcTemplateGenerator(templateCopy, compsCopy)
    return funcTemplate

def generateFuncTemplate(path):
    assert isinstance(path, str)
    with open(path, 'r') as f:
        template = f.read()
    comps = re.findall('\{\{(?:(?!}}).)*}}', template)
    comps.reverse()
    comps = OrderedDict(zip([i[2:-2] for i in comps], repeat(None)))
    return funcTemplateGenerator(template, comps)
