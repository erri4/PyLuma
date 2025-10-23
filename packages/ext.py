from LumaExtBundle import Raw, DictToDict, ParseMe, Function

print("this is an example python extention.")


def func(arg=""):
    return ParseMe({"type": "str", "args": [Raw("stringhbhbiyb" + str(arg))]})

def funccls(this=None):
    print("this." + this.value)

# TODO: add class support

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
