'  The Imports (Do not change anything right here)  '
from UtilsDirectory.data import *

'  Enable Intents due to discord making us enable intents to get the member list   '
intents = discord.Intents.all()

'  The Bot prefix and using intents.  '
bot = commands.Bot(command_prefix=dc_prefix, intents=intents)

'  The Botstart  '
@bot.event
async def on_ready():
    print(f"Es hora de jugar [3/3]")
    print(f"Servers donde hay {bot.user.name}:",
          len(bot.guilds))
    bot.loop.create_task(status_task(bot))


'  The Statustask  '
async def status_task(bot):
    while True:
        await bot.change_presence(activity=discord.Game(name="mirar cualrdos"))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(name="Tirar billetes"))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(name="no estar jugando"))
        await asyncio.sleep(15)


'  The Errorhandling  '
@bot.event
async def on_command_error(ctx, error):
    print(f"{ctx.guild.name}:  {error}")  # Consolemessage
    if isinstance(error, commands.CommandError):
        await ctx.send(f">>> **Hay un error!** (Mira tu consola!)\n{error}")  # Errormessage


'  Raiding Area (All Commands listed)  '
for filename in os.listdir('EntireRaid'):
    if filename.endswith('.py'):
        bot.load_extension(f'EntireRaid.{filename[:-3]}')
print("\033[91;1m... Listo! [1/3]")
for filename in os.listdir('RaidModules'):
    if filename.endswith('.py'):
        bot.load_extension(f'RaidModules.{filename[:-3]}')
print("... Listo! [2/3]")

bot.remove_command('help')
bot.run(dc_token)
