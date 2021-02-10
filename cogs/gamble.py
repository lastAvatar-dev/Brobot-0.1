from discord.ext import commands
import random

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ctx.message.author, ctx.message.content,"  ->ex  ", ex)
        await ctx.send(ex)
        
    @commands.command(brief="   Get a random number.")
    async def random(self, ctx):
        n = random.randrange(1, 100)
        await ctx.send(n)
    
    @commands.command(brief="   Roll the dice.")
    async def dice(self, ctx):
        n = random.randrange(1,6)
        await ctx.send(n)

    @commands.command(brief="   Flip a coin.")
    async def coin(self, ctx):
        n = random.randint(0, 1)
        await ctx.send("Head" if n == 1 else "Tail")
    
def setup(bot):
    bot.add_cog(Gamble(bot))
