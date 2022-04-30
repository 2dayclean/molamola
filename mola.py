from doctest import debug_script
from pydoc import describe
import discord
import random
from to import Token as token
from discord.commands import Option

guildid=[969822576434106428]

class Mola:
    gen = 0
    level = 1
    exp = 0
    maxexp = 5
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.maxexp = self.level * 3

    def draw(self):
        desc = "개복치의 세대 : {}\n개복치의 레벨 :{} \n개복치의 경험치 : {}/{} ({:.2f} %)".format(self.gen, self.level, self.exp, self.maxexp, self.exp/self.maxexp * 100)
        return desc
    
    def initialize(self):
        self.gen += 1
        self.level = 1
        self.exp = 0
        self.maxexp = self.level * 3

    def die(self):
        self.initialize()

    def feed(self, food): #food는 [이름, 경험치, 사망확률]
        cache = random.randint(1, 100)
        if cache <= food[2]:
            self.die()
            return -1
        else:
            self.exp += food[1]
            counter = self.lvup()
            return counter
    
    def lvup(self):
        cnt = 0
        while self.exp >= self.maxexp:
            self.exp -= self.maxexp
            self.level += 1
            self.maxexp = self.level * 3
            cnt += 1
        return cnt

bot = discord.Bot()
mola = Mola()

@bot.event
async def on_ready():
    print("봇이 이제 작동합니다.")

@bot.slash_command(guild_ids = guildid, description = "개복치에게 먹이를 줍니다")
async def feed(
    ctx,
    text: Option(str, "먹이", choices=["정어리", "새우"])
    ):
    if text == "정어리":
        resp = mola.feed(["정어리", 1, 5])
        desc = mola.draw()
    elif text == "새우":
        resp = mola.feed(["새우", 3, 18])
        desc = mola.draw()
    if resp == -1:
        desc = "***개복치가 죽어버려 다른 개복치를 사왔다.\n\n"+desc
    elif resp != 0:
        desc = "***개복치의 레벨이 올랐다.\n\n"+desc
    embed = discord.Embed(title="개복치에게 먹이를 주었다!", description=desc, color = 0xFFFFFF)
    embed.set_footer(text="molamola corp.")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_ids=guildid, description = "개복치의 상태를 봅니다.")
async def info(ctx):
    desc = mola.draw()
    embed = discord.Embed(title="개복치의 정보창을 열어보았다!", description=desc, color = 0xFFFFFF)
    embed.set_footer(text="molamola corp.")
    await ctx.respond(embed = embed)

@bot.slash_command(guild_ids=guildid, aliases = [''], description = "먹이의 정보를 봅니다")
async def foods(ctx):
    desc = f"정어리 : 경험치 + 1, 사망확률 5%\n새우 : 경험치 + 3, 사망확률 18%"
    embed = discord.Embed(title="먹이정보", description=desc, color = 0xFFFFFF)
    embed.set_footer(text="molamola corp.")
    await ctx.respond(embed = embed)


bot.run(token)