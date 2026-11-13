from LumaExtBundle import Raw, ParseMe, Function, Class
from LumaTypes import LumaInterpreter
import json

def constructor_str(value, this: LumaInterpreter.InstancedLumaObject | None = None):
    if type(value) is this.expose("InstancedLumaObject"):
        if value.typename == "str":
            this.value = value.value
            return
    this.value = str(value)
constructor_str.__name__ = "constructor"


def add(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["str"].instance([this.value + str(other)])
add.__name__ = "@addition"

def eq(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value == str(other)])
eq.__name__ = "@eq"

def neq(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value != str(other)])
neq.__name__ = "@neq"

def intify(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["int"].instance([int(this.value)])
intify.__name__ = "@int"


def at(pos, this: LumaInterpreter.InstancedLumaObject | None = None):
    env = this.expose("env")
    if pos.typename == "int":
        return env[0]["str"].instance([this.value[pos.children["value"]]])
    else:
        this.expose("throw")(
            env[0]["typeError"],
            "str key must be an integer",
            "internal",
            "internal",
            this.expose("filename"),
        )
at.__name__ = "@at"


def stringify_str(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["str"].instance([this.value])
stringify_str.__name__ = "@stringify"


def repre(this: LumaInterpreter.InstancedLumaObject | None = None):
    if '"' in this.value and "'" not in this.value:
        return this.expose("env")[0]["str"].instance(["'" + this.value + "'"])
    if "'" in this.value and '"' not in this.value:
        return this.expose("env")[0]["str"].instance(['"' + this.value + '"'])
    return this.expose("env")[0]["str"].instance([json.dumps(this.value)])
repre.__name__ = "@repr"


def length(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["int"].instance([len(this.value)])
length.__name__ = "len"


def lbool(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["bool"].instance([len(this.value)])
lbool.__name__ = "@bool"

def constructor(this: LumaInterpreter.InstancedLumaObject | None = None):
    pass

LumaExtension = {
    "Object": Class(
        "Object",
        Function(constructor, [{"name": "this"}])
    ),
    "str": Class(
        "str",
        Function(constructor_str, [{"name": "this"}, {"name": "value"}]),
        [
            Function(add, [{"name": "this"}, {"name": "other"}]),
            Function(eq, [{"name": "this"}, {"name": "other"}]),
            Function(neq, [{"name": "this"}, {"name": "other"}]),
            Function(intify, [{"name": "this"}]),
            Function(at, [{"name": "this"}, {"name": "pos"}]),
            Function(stringify_str, [{"name": "this"}]),
            Function(repre, [{"name": "this"}]),
            Function(length, [{"name": "this"}]),
            Function(lbool, [{"name": "this"}]),
        ],
    ),
}
