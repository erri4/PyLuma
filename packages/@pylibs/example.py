from LumaExtBundle import Raw, DictToDict, ParseMe, Function, Class
from LumaTypes import LumaInterpreter

print("This is an example python extention. This has no (practical or not) use.")

def func(arg=""):
    return ParseMe({"type": "str", "args": [Raw("stringhbhbiyb" + str(arg))]})

def funccls(this: LumaInterpreter.InstancedLumaObject = None):
    print("this." + this.value)

LumaExtension = {
    "test": {
        "type": "list",
        "name": "test",
        "args": [
            Raw(
                DictToDict(
                    [{"type": "int", "args": [Raw(0)]}],
                    [{"type": "str", "args": [Raw("hi")]}],
                )
            )
        ],
    },
    "mycls": Class('mycls', None, [Function(funccls, [])], parent="str"),
    "func": Function(func, [{"name": "arg", "default": Raw("")}]),
}
