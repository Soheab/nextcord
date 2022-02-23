
from __future__ import annotations
import nextcord
from nextcord import SlashOption
from nextcord.ext import commands


bot = commands.Bot(command_prefix=".?")


@bot.slash_command(name="ping", guild_ids=[890673374731321395])
@bot.command(name="ping")
async def get_bot_ping(ctx):
    print(ctx, type(ctx), dir(ctx), ctx.command, type(ctx.command))
    await ctx.send(
        embed=nextcord.Embed(description=f"**My ping: {round(bot.latency,1)} ms**", color=nextcord.Color.green())
    )

class Cag(commands.Cog):
    @nextcord.slash_command(name="pingcog", guild_ids=[890673374731321395])
    @commands.command(name="pingcog")

    async def get_bot_ping_cog(self, ctx):
        print(ctx, type(ctx), dir(ctx), ctx.command, type(ctx.command))
        await ctx.send(
            embed=nextcord.Embed(description=f"**My ping: {round(bot.latency,1)} ms**", color=nextcord.Color.green())
        )

bot.add_cog(Cag())
bot.run("lol")
