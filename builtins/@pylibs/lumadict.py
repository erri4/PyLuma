from LumaExtBundle import Raw, ParseMe, Function, Class
from LumaTypes import LumaInterpreter


def constructor_dict(value: dict, this: LumaInterpreter.InstancedLumaObject | None = None):
    this.value = value.copy()
constructor_dict.__name__ = 'constructor'

def at(pos, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.value[pos]
at.__name__ = '@at'

def delat(pos, this: LumaInterpreter.InstancedLumaObject | None = None):
    del this.value[pos]
delat.__name__ = '@del'

def del_(pos, this: LumaInterpreter.InstancedLumaObject | None = None):
    del this.value[pos]
del_.__name__ = 'del_'

def intify_dict(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]["int"].instance([len(this.value)])
intify_dict.__name__ = '@int'

def dctset(pos, value, this: LumaInterpreter.InstancedLumaObject | None = None) -> None:
    this.value[pos] = value
dctset.__name__ = '@set'

def stringify_dict(this: LumaInterpreter.InstancedLumaObject | None = None):
    dct = "{"
    items = list(this.value.items())
    for i in range(len(items)):
        k, v = items[i][0], items[i][1]
        dct += (
            repr(k)
            + ": "
            + repr(v)
            + (", " if i + 1 in range(len(items)) else "")
        )
    dct += "}"
    return this.expose('env')[0]["str"].instance(
        [dct],
    )
stringify_dict.__name__ = '@stringify'

def repr_dict(this: LumaInterpreter.InstancedLumaObject | None = None):
                dct = "{"
                items = list(this.value.items())
                for i in range(len(items)):
                    k, v = items[i][0], items[i][1]
                    dct += (
                        repr(k)
                        + ": "
                        + repr(v)
                        + (", " if i + 1 in range(len(items)) else "")
                    )
                dct += "}"
                return this.expose('env')[0]["str"].instance(
                    [dct],
                )
repr_dict.__name__ = '@repr'

def eq_dict(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value == dict(other)])
eq_dict.__name__ = "@eq"

def neq_dict(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value != dict(other)])
neq_dict.__name__ = "@neq"

def selfdict(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this
selfdict.__name__ = "@dict"

def length(this: LumaInterpreter.InstancedLumaObject | None = None):
    int_ = this.expose('env')[0]["int"]
    obj = int_.instance([len(this.value)])
    return obj
length.__name__ = 'len'

def lbool(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]["bool"].instance([bool(len(this.value))])
lbool.__name__ = '@bool'


LumaExtension = {
    "dict": Class(
        "dict",
        Function(
            constructor_dict,
            [{"name": "this"}, {"name": "value"}]
        ),
        [
            Function(at, [{"name": "this"}, {"name": "pos"}]),
            Function(delat, [{"name": "this"}, {"name": "pos"}]),
            Function(del_, [{"name": "this"}, {"name": "pos"}]),
            Function(intify_dict, [{"name": "this"}]),
            Function(dctset, [{"name": "this"}, {"name": "pos"}, {"name": "value"}]),
            Function(stringify_dict, [{"name": "this"}]),
            Function(repr_dict, [{"name": "this"}]),
            Function(length, [{"name": "this"}]),
            Function(lbool, [{"name": "this"}]),
            Function(selfdict, [{"name": "this"}]),
            Function(eq_dict, [{"name": "this"}, {"name": "other"}]),
            Function(neq_dict, [{"name": "this"}, {"name": "other"}]),
        ]
    ),
}