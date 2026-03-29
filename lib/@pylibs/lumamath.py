from LumaExtBundle import Raw, ParseMe, Function
import math

LumaExtension = {
    "pi": {
        "type": "float",
        "args": [Raw(math.pi)],
    },
    "e": {
        "type": "float",
        "args": [Raw(math.e)],
    },
    "sin": Function(
        lambda x: ParseMe(
            {"type": "float", "args": [Raw(math.sin(float(x)))]}
        ),
        [{"name": "x"}],
    ),
    "arcsin": Function(
        lambda x: ParseMe(
            {"type": "float", "args": [Raw(math.asin(float(x)))]}
        ),
        [{"name": "x"}],
    ),
    "cos": Function(
        lambda x: ParseMe(
            {"type": "float", "args": [Raw(math.cos(float(x)))]}
        ),
        [{"name": "x"}],
    ),
    "arccos": Function(
        lambda x: ParseMe(
            {"type": "float", "args": [Raw(math.acos(float(x)))]}
        ),
        [{"name": "x"}],
    ),
    "tan": Function(
        lambda x: ParseMe(
            {"type": "float", "args": [Raw(math.tan(float(x)))]}
        ),
        [{"name": "x"}],
    ),
    "arctan": Function(
        lambda x: ParseMe(
            {"type": "float", "args": [Raw(math.atan(float(x)))]}
        ),
        [{"name": "x"}],
    ),
    "sqrt": Function(
        lambda x: ParseMe(
            {"type": "float", "args": [Raw(math.sqrt(float(x)))]}
        ),
        [{"name": "x"}],
    ),
}
