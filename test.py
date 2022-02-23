
import nextcord
from nextcord import SlashOption
from nextcord.ext import commands


bot = commands.Bot(command_prefix=".?")


@bot.command(name="ping")
@bot.slash_command(name="ping2", guild_ids=[890673374731321395])
async def get_bot_ping(ctx, hello: str):
    print(ctx, type(ctx), dir(ctx), ctx.command, type(ctx.command))
    await ctx.send(
        embed=nextcord.Embed(description=f"**My ping: {round(bot.latency,1)} ms**", color=nextcord.Color.green())
    )

class Cag(commands.Cog):
    @commands.command(name="pingcog")
    @nextcord.slash_command(name="ping2cog", guild_ids=[890673374731321395])

    async def get_bot_ping_cog(self, ctx, hello: str):
        print(ctx, type(ctx), dir(ctx), ctx.command, type(ctx.command))
        await ctx.send(
            embed=nextcord.Embed(description=f"**My ping: {round(bot.latency,1)} ms**", color=nextcord.Color.green())
        )

bot.add_cog(Cag())
bot.run("KEKW")
