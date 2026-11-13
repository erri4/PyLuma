from LumaExtBundle import Raw, ParseMe, Function, Class
from LumaTypes import LumaInterpreter

def constructor_err(msg, this: LumaInterpreter.InstancedLumaObject | None = None):
    setattr(this, "msg", msg)
    setattr(this, "tb", this.expose("traceback")())
constructor_err.__name__ = "constructor"


def trigger(this: LumaInterpreter.InstancedLumaObject | None = None):
    raise this.expose("LumaException")(this)


def stringify_err(this: LumaInterpreter.InstancedLumaObject | None = None):
    return getattr(this, "msg")
stringify_err.__name__ = "@stringify"


def show(data = "", end = '\n'):
    print(data, end=str(end))

def inpt(prompt = ""):
    return ParseMe({"type": 'str', 'args': [Raw(input(prompt))]})
inpt.__name__ = 'input'


LumaExtension = {
    "baseError": Class(
        "baseError",
        Function(
            constructor_err,
            [
                {"name": "this"},
                {"name": "msg", "default": {"type": "str", "args": [Raw("")]}},
            ],
        ),
        [
            Function(trigger, [{"name": "this"}]),
            Function(stringify_err, [{"name": "this"}]),
        ],
    ),
    "show": Function(show, [
        {"name": "data", "default": {"type": "str", "args": [Raw("")]}},
        {"name": "end", "default": {"type": "str", "args": [Raw("\n")]}},
    ]),
    "input": Function(inpt, [
        {"name": "prompt", "default": {"type": "str", "args": [Raw("")]}}
    ]),
}
