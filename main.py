from twitchio.ext import commands 
import config
import asyncio

val = input("Enter your channel name: ")
val2 = input("Enter second channel's name: ")

class Bot(commands.Bot):
    
    
    
    def __init__(self):

        super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2])


    async def event_message(self, messagae):

        print(f'Logged in as | {self.nick}')
        print(f'user id is | {self.user_id}')

    async def event_message(self, message):

        if message.echo:
            return
        
        print(message.content)

        await self.handle_commands(message)

    
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}')


bot = Bot()
bot.run()

