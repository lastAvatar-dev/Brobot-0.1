from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(brief="   Create a link to invite new people to this cool server.")
    @commands.guild_only()
    async def invite(self, ctx, max_age, max_uses):
        link = await ctx.channel.create_invite(max_age=max_age,max_uses=max_uses)
        await ctx.send(link)

def setup(bot):
    bot.add_cog(Utils(bot))