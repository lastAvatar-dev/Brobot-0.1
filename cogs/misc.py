from discord.ext import commands
from utils import text_to_owo
class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ctx.message.author, ctx.message.content,"  ->ex  ", ex)
        await ctx.send(ex)
        
    @commands.command(brief="   Repeat a message.")
    async def echo(self, ctx, *args):
        await ctx.send(" ".join(args))

    @commands.command(brief="   The best twanswatow to impwess youw fwiend (・`ω´・)")
    async def owo(self, ctx, *args):
        await ctx.send(text_to_owo(" ".join(args)))

def setup(bot):
    bot.add_cog(Misc(bot))