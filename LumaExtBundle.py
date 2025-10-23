class Raw:
    def __init__(self, data):
        self.data = data


class DictToDict:
    def __init__(self, keys: list = [], values: list = []):
        self.keys = keys
        self.values = values

    def __getitem__(self, key):
        return self.values[self.keys.index(key)]
    
class ParseMe:
    def __init__(self, data: dict):
        self.data = data

def Function(f, args):
    return {
        "type": "functionType",
        "name": f.__name__,
        "body": f,
        "args": args,
    }
