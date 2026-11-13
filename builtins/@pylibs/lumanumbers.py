from LumaExtBundle import Raw, ParseMe, Function, Class
from LumaTypes import LumaInterpreter

def constructor(value, this: LumaInterpreter.InstancedLumaObject | None = None):
    if type(value) is this.expose("InstancedLumaObject"):
        if value.typename == "int":
            this.value = value.value
            return
    this.value = int(value)
constructor.__name__ = "constructor"

def eq(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value == int(other)])
eq.__name__ = "@eq"

def neq(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value != int(other)])
neq.__name__ = "@neq"

def leq(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value <= int(other)])
leq.__name__ = '@leq'

def lt(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value < int(other)])
lt.__name__ = '@lt'

def geq(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value >= int(other)])
geq.__name__ = '@geq'

def gt(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value > int(other)])
gt.__name__ = '@gt'

def add(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    if type(other) is this.expose('InstancedLumaObject'):
        if other.typename == 'float':
            return this.expose("env")[0]["float"].instance([this.value + float(other)])
    return this.expose("env")[0]["int"].instance([this.value + int(other)])
add.__name__ = "@addition"

def sub(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    if type(other) is this.expose('InstancedLumaObject'):
        if other.typename == 'float':
            return this.expose("env")[0]["float"].instance([this.value - float(other)])
    return this.expose("env")[0]["int"].instance([this.value - int(other)])
sub.__name__ = "@subtraction"

def division(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["int"].instance([this.value // int(other)])
division.__name__ = "@division"

def multiplication(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    if type(other) is this.expose('InstancedLumaObject'):
        if other.typename == 'float':
            return this.expose("env")[0]["float"].instance([this.value * float(other)])
    return this.expose("env")[0]["int"].instance([this.value * int(other)])
multiplication.__name__ = "@multiplication"

def modulus(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["int"].instance([this.value % int(other)])
modulus.__name__ = "@modulus"

def power(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    if type(other) is this.expose('InstancedLumaObject'):
        if other.typename == 'float':
            return this.expose("env")[0]["float"].instance([this.value ** float(other)])
    return this.expose("env")[0]["int"].instance([this.value ** int(other)])
power.__name__ = "@power"

def shift_r(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["int"].instance([this.value >> int(other)])
shift_r.__name__ = "@shift_r"

def shift_l(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["int"].instance([this.value << int(other)])
shift_l.__name__ = "@shift_l"

def stringify(this: LumaInterpreter.InstancedLumaObject | None = None):
    return ParseMe({"type": "str", "args": [Raw(str(this.value))]})
stringify.__name__ = '@stringify'

def repre(this: LumaInterpreter.InstancedLumaObject | None = None):
    return ParseMe({"type": "str", "args": [Raw(repr(this.value))]})
repre.__name__ = '@repr'

def intify(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this
intify.__name__ = '@int'

def floatify(this: LumaInterpreter.InstancedLumaObject | None = None):
    return ParseMe({"type": "float", "args": [Raw(float(this.value))]})
floatify.__name__ = '@float'

def lbool(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["bool"].instance([bool(this.value)])
lbool.__name__ = "@bool"



def constructor_float(value, this: LumaInterpreter.InstancedLumaObject | None = None):
    if type(value) is this.expose("InstancedLumaObject"):
        if value.typename == "float":
            this.value = value.value
            return
    this.value = float(value)
constructor_float.__name__ = "constructor"

def eq_float(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value == float(other)])
eq_float.__name__ = "@eq"

def neq_float(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value != float(other)])
neq_float.__name__ = "@neq"

def leq_float(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value <= float(other)])
leq_float.__name__ = '@leq'

def lt_float(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value < float(other)])
lt_float.__name__ = '@lt'

def geq_float(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value >= float(other)])
geq_float.__name__ = '@geq'

def gt_float(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose('env')[0]['bool'].instance([this.value > float(other)])
gt_float.__name__ = '@gt'

def add_float(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["float"].instance([this.value + float(other)])
add_float.__name__ = "@addition"

def sub_float(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["float"].instance([this.value - float(other)])
sub_float.__name__ = "@subtraction"

def division_float(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["float"].instance([this.value / float(other)])
division_float.__name__ = "@division"

def multiplication_float(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["float"].instance([this.value * float(other)])
multiplication_float.__name__ = "@multiplication"

def power_float(other, this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["float"].instance([this.value ** float(other)])
power_float.__name__ = "@power"

def stringify_float(this: LumaInterpreter.InstancedLumaObject | None = None):
    return ParseMe({"type": "str", "args": [Raw(str(this.value))]})
stringify_float.__name__ = '@stringify'

def repre_float(this: LumaInterpreter.InstancedLumaObject | None = None):
    return ParseMe({"type": "str", "args": [Raw(repr(this.value))]})
repre_float.__name__ = '@repr'

def intify_float(this: LumaInterpreter.InstancedLumaObject | None = None):
    return ParseMe({"type": "int", "args": [Raw(int(this.value))]})
intify_float.__name__ = '@int'

def floatify_float(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this
floatify_float.__name__ = '@float'

def lbool_float(this: LumaInterpreter.InstancedLumaObject | None = None):
    return this.expose("env")[0]["bool"].instance([bool(this.value)])
lbool_float.__name__ = "@bool"

LumaExtension = {
    "int": Class(
        "int",
        Function(
            constructor,
            [{"name": "this"}, {"name": "value"}]
        ),
        [
            Function(eq, [{"name": "this"}, {"name": "other"}]),
            Function(neq, [{"name": "this"}, {"name": "other"}]),
            Function(leq, [{"name": "this"}, {"name": "other"}]),
            Function(geq, [{"name": "this"}, {"name": "other"}]),
            Function(gt, [{"name": "this"}, {"name": "other"}]),
            Function(lt, [{"name": "this"}, {"name": "other"}]),
            Function(add, [{"name": "this"}, {"name": "other"}]),
            Function(sub, [{"name": "this"}, {"name": "other"}]),
            Function(multiplication, [{"name": "this"}, {"name": "other"}]),
            Function(division, [{"name": "this"}, {"name": "other"}]),
            Function(modulus, [{"name": "this"}, {"name": "other"}]),
            Function(power, [{"name": "this"}, {"name": "other"}]),
            Function(shift_l, [{"name": "this"}, {"name": "other"}]),
            Function(shift_r, [{"name": "this"}, {"name": "other"}]),
            Function(stringify, [{"name": "this"}]),
            Function(repre, [{"name": "this"}]),
            Function(intify, [{"name": "this"}]),
            Function(floatify, [{"name": "this"}]),
            Function(lbool, [{"name": "this"}]),
        ]
    ),
    "float": Class(
        "float",
        Function(
            constructor_float,
            [{"name": "this"}, {"name": "value"}]
        ),
        [
            Function(eq_float, [{"name": "this"}, {"name": "other"}]),
            Function(neq_float, [{"name": "this"}, {"name": "other"}]),
            Function(leq_float, [{"name": "this"}, {"name": "other"}]),
            Function(geq_float, [{"name": "this"}, {"name": "other"}]),
            Function(gt_float, [{"name": "this"}, {"name": "other"}]),
            Function(lt_float, [{"name": "this"}, {"name": "other"}]),
            Function(add_float, [{"name": "this"}, {"name": "other"}]),
            Function(sub_float, [{"name": "this"}, {"name": "other"}]),
            Function(multiplication_float, [{"name": "this"}, {"name": "other"}]),
            Function(division_float, [{"name": "this"}, {"name": "other"}]),
            Function(power_float, [{"name": "this"}, {"name": "other"}]),
            Function(stringify_float, [{"name": "this"}]),
            Function(repre_float, [{"name": "this"}]),
            Function(intify_float, [{"name": "this"}]),
            Function(floatify_float, [{"name": "this"}]),
            Function(lbool_float, [{"name": "this"}]),
        ]
    ),
}