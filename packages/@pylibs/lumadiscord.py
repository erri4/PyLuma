import discord
from discord.ext import commands
from LumaExtBundle import ParseMe, Raw, Function
from LumaTypes import LumaInterpreter
import asyncio

def constructor(this=None, prefix = '!'):
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=str(prefix), intents=intents)
    setattr(this, 'bot', bot)

def add_command(this: LumaInterpreter.InstancedLumaObject | None = None, name = None, func: LumaInterpreter.LumaFunction = None):
    @this.bot.command(name=str(name))
    async def cmd(ctx):
        func.run([ParseMe({"type": "Context", "args": [Raw(ctx)]})])

def run(this=None, token = None):
    assert token is not None
    this.bot.run(str(token))

def Context(this = None, ctx: commands.Context = None):
    assert ctx is not None
    setattr(this, 'ctx', ctx)

def send(this=None, msg = None):
    assert msg is not None
    asyncio.create_task(this.ctx.send(str(msg)))

def exit(this=None):
    this.bot.loop.call_soon_threadsafe(lambda: asyncio.create_task(this.bot.close()))

LumaExtension = {
    "Bot": {
        "type": "classType",
        "name": "Bot",
        "constructor": Function(constructor, [{"name": "this"}, {'name': 'prefix'},]),
        "functions": [Function(run, [{"name": "this"}, {'name': 'token'}]), Function(add_command, [{"name": "this"}, {'name': 'name'}, {'name': 'func'}]), Function(exit, [{"name": "this"},])],
        "classes": [],
        "vars": [],
        "parent": [],
    },
    "Context": {
        "type": "classType",
        "name": "Context",
        "constructor": Function(Context, [{"name": "this"}, {'name': 'ctx'}]),
        "functions": [Function(send, [{"name": "this"}, {'name': 'msg'}])],
        "classes": [],
        "vars": [],
        "parent": [],
    }
}
