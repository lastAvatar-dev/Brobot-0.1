import discord
import aiohttp
from discord.ext import commands

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief="   Show a ramdom cat picture.")
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="meow")
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="http://random.cat")

                    await ctx.send(embed=embed)

    @commands.command(brief="   Show a ramdom dog picture.")
    async def dog(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()

                    embed = discord.Embed(title="woof")
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="https://random.dog")

                    await ctx.send(embed=embed)

    @commands.command(brief="   Show a random fox picture.")
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://randomfox.ca/floof/") as r:
                    data = await r.json()

                    embed = discord.Embed(title="floof")
                    embed.set_image(url=data['image'])
                    embed.set_footer(text="https://randomfox.ca")

                    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Images(bot))