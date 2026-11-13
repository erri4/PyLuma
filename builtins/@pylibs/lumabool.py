from LumaExtBundle import Raw, ParseMe, Function, Class
from LumaTypes import LumaInterpreter

def constructor_bool(
    value: LumaInterpreter.InstancedLumaObject, this: LumaInterpreter.InstancedLumaObject | None = None
) -> None:
    if type(value) is this.expose("InstancedLumaObject"):
        this.value = bool(value.__lbool__())
    else:
        this.value = bool(value)
constructor_bool.__name__ = "constructor"

def eq_bool(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value == bool(other)])
eq_bool.__name__ = "@eq"

def neq_bool(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value != bool(other)])
neq_bool.__name__ = "@neq"

def intify_bool(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose()("env")[0]["int"].instance([int(this.value)])
intify_bool.__name__ = "@int"


def stringify_bool(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["str"].instance([str(this.value).lower()])
stringify_bool.__name__ = "@stringify"


def selfbool(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this
selfbool.__name__ = "@bool"


def repr_bool(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["str"].instance([str(this.value).lower()])
repr_bool.__name__ = "@repr"

LumaExtension = {
    "bool": Class(
        "bool",
        Function(constructor_bool, [{"name": "this"}, {"name": "value"}]),
        [
            Function(intify_bool, [{"name": "this"}]),
            Function(stringify_bool, [{"name": "this"}]),
            Function(repr_bool, [{"name": "this"}]),
            Function(selfbool, [{"name": "this"}]),
            Function(eq_bool, [{"name": "this"}, {"name": "other"}]),
            Function(neq_bool, [{"name": "this"}, {"name": "other"}]),
        ],
    ),
}