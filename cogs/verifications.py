from discord.ext import commands
from twilio.rest import Client
from settings import ACCOUNT_SID, AUTH_TOKEN

client = Client(ACCOUNT_SID, AUTH_TOKEN)


class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(brief="Send verification code to your phone number.")
    async def verify(self, ctx, phone_number):
        phone = phone_number.replace("0", "+84", 1)
        service = client.verify.services.create(friendly_name='Discord')
        verification = client.verify \
                     .services(service.sid) \
                     .verifications \
                     .create(to=phone, channel='sms')
        await ctx.send("Your verification code is being send to {phone_number}.\nPlease use auth command to verify your account!")

    @commands.command(brief="Submit your verification code for authentication.")
    async def auth(self, ctx, verification_code):
        verification_check = client.verify \
                           .services(service.sid) \
                           .verification_checks \
                           .create(to='+84337342614', code=verification_code)

        stt = verification_check.status


def setup(bot):
    bot.add_cog(Verification(bot))