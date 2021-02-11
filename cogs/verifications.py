from discord.ext import commands
from twilio.rest import Client
from settings import ACCOUNT_SID, AUTH_TOKEN

client = Client(ACCOUNT_SID, AUTH_TOKEN)


class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def verify(self, ctx, phonenumber):
        phone = phonenumber.replace("0", "+84", 1)
        service = client.verify.services.create(friendly_name='Discord')
        verification = client.verify \
                     .services(service.sid) \
                     .verifications \
                     .create(to=phone, channel='sms')

        

def setup(bot):
    bot.add_cog(Verification(bot))