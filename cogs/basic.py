from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ctx.message.author, ctx.message.content,"  ->ex  ", ex)
        await ctx.send(ex)
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

def setup(bot):
    bot.add_cog(Basic(bot))