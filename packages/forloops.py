from LumaExtBundle import Overload
import LumaTypes

def process(self: LumaTypes.LumaInterpreter, line: str, linenum: int, Object = None, file: str = ''):
    self.SAVED_KEYWORDS.append('for') if not 'for' in self.SAVED_KEYWORDS else None
    if line.startswith('for'):
        counter = self.smrtsplt(line[line.find('(')+ 1:line.rfind(')')].strip(), ', ')
        self.process(counter[0], linenum)
        program = self.scopes[-1]
        body = ''
        for subline in program.splitlines()[linenum:]:
            if subline[0] == '}':
                break
            body += subline + "\n"
        body = body.strip()
        while self.evaluate(counter[1]):
            self.runsubprogram(body, Object, line1=linenum + 1, file=file)
            self.process(counter[2], linenum)
        return True
    return False

LumaExtension = {
    "forloops": {
        "type": Overload("beforeprocess"),
        "function": process
    },
}
