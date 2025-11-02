from LumaExtBundle import Overload
import LumaTypes

def process(self: LumaTypes.LumaInterpreter, line: str, linenum: int, Object = None, file: str = ''):
    self.SAVED_KEYWORDS.append('for') if not 'for' in self.SAVED_KEYWORDS else None
    if line.startswith('for'):
        counter = self.smrtsplt(line[line.find('(')+ 1:line.rfind(')')].strip(), ', ')
        varname = counter[0][4 : counter[0].find("to") - 1]
        value = self.evaluate(counter[0][counter[0].find("to") + 3 :], varname)
        if varname in self.SAVED_KEYWORDS:
            self.throw(
                self.env["typeError"],
                f"cannot assign to '{varname}': saved keyword",
            )
        program = self.scopes[-1]
        self.env[varname] = value
        body = ''
        for subline in program.splitlines()[linenum:]:
            if subline[0] == '}':
                break
            body += subline + "\n"
        body = body.strip()
        while self.evaluate(counter[1]):
            self.runsubprogram(body, Object, line1=linenum + 1, file=file)
            self.env[varname] = self.evaluate(counter[2])
        del self.env[varname]
        return True
    return False

LumaExtension = {
    "overload": {
        "type": Overload("process"),
        "function": process
    },
}
