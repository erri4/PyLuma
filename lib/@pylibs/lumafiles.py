from LumaExtBundle import Raw, ParseMe, Function, Class
from LumaTypes import LumaInterpreter

def constructor(path, this: LumaInterpreter.InstancedLumaObject | None = None):
    this.path = str(path)

def read(this: LumaInterpreter.InstancedLumaObject | None = None):
    with open(this.path) as f:
        return ParseMe({'type': 'str', 'args': [Raw(f.read())]})

def write(newfile, this: LumaInterpreter.InstancedLumaObject | None = None):
    with open(this.path, 'w') as f:
        f.write(str(newfile))

def writeln(line, this: LumaInterpreter.InstancedLumaObject | None = None):
    with open(this.path, 'a') as f:
        f.write('\n' + str(line))

LumaExtension = {
    "file": Class(
        "file",
        Function(constructor, [{"name": "this"}, {"name": "path"}]),
        [
            Function(read, [{"name": "this"}]),
            Function(write, [{"name": "this"}, {"name": "newfile"}]),
            Function(writeln, [{"name": "this"}, {"name": "line"}]),
        ],
    ),
}
