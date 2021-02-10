import discord
from discord.ext import commands
from utils import get_mama_jokes

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(brief="   Insult someone.")
    async def insult(self, ctx, member: discord.Member = None):
        insult = await get_mama_jokes()
        await ctx.send(f"<@!{member.id}> {insult}")

def setup(bot):
    bot.add_cog(NSFW(bot))