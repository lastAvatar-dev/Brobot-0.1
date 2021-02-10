from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ctx.message.author, ctx.message.content,"  ->ex  ", ex)
        await ctx.send(ex)
        
    @commands.command(brief="   Create a link to invite new people to this cool server.")
    @commands.guild_only()
    async def invite(self, ctx, *args):
        link = await ctx.channel.create_invite(max_age=60)
        await ctx.send(link)


def setup(bot):
    bot.add_cog(Utils(bot))