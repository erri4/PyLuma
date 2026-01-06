from typing import TypedDict, TypeVar

class Raw:
    def __init__(self, data):
        self.data = data

class DictToDict:
    def __init__(self, keys: list = [], values: list = []):
        self.keys = keys
        self.values = values

    def __getitem__(self, key):
        return self.values[self.keys.index(key)]
    
class Override:
    def __init__(self, funcname):
        self.funcname = funcname

class Overload:
    def __init__(self, funcname):
        self.funcname = funcname
    
class ParseMe:
    def __init__(self, data: dict):
        self.data = data

EvaluatedType = TypeVar('EvaluatedType')

class Arg(TypedDict):
    name: str
    default: EvaluatedType

def Function(f, args: list[Arg]):
    return {
        "type": "functionType",
        "name": f.__name__,
        "body": f,
        "args": args,
    }
