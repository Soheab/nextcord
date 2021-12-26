import nextcord
from nextcord.ext import commands


bot = commands.Bot(command_prefix=".?")


@bot.command(name="ping")
@bot.slash_command(name="ping2", guild_ids=[890673374731321395])
async def get_bot_ping(ctx):
    print(ctx, type(ctx), dir(ctx))
    await ctx.send(
        embed=nextcord.Embed(description=f"**My ping: {round(bot.latency,1)} ms**", color=nextcord.Color.green())
    )


bot.run("lol nice")
