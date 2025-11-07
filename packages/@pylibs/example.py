from LumaExtBundle import Raw, DictToDict, ParseMe, Function

print("This is an example python extention. This has no (practical or not) use.")

def func(arg=""):
    return ParseMe({"type": "str", "args": [Raw("stringhbhbiyb" + str(arg))]})

def funccls(this=None):
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
    "mycls": {
        "type": "classType",
        "name": "mycls",
        "constructor": None,
        "functions": [Function(funccls, [])],
        "classes": [],
        "vars": [],
        "parent": "str",
    },
    "func": Function(func, [{"name": "arg", "default": Raw("")}]),
}
