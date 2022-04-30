import discord
from to import Token as token
from discord.commands import Option

bot = discord.Bot()

@bot.event
async def on_ready():
    print("봇이 작동합니다.")

@bot.slash_command(description="Check bot's response latency")
async def ping(ctx):
    embed = discord.Embed(title="Pong!", description=f"Delay: {bot.latency} seconds", color=0xFFFFFF)
    embed.set_footer(text="Embed Footer")
    await ctx.respond(embed=embed)

@bot.slash_command()
async def feed(
    ctx,
    text: Option(str, "목록 : ", choices=["1","2"]),
):
    if text == "1":
        await ctx.respond(f"선택된 문자열: {text}")
    elif text == "2":
        await ctx.respond("와 쌘즈")

bot.run(token)