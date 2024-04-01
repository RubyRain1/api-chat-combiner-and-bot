from twitchio.ext import commands 
import config
import asyncio
from abcs import Messageable
from typing import Optional, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from user import User
    from websocket import WSConnection
    
val = input("Enter your channel name: ")
val2 = input("Enter second channel's name: ")
       
            


class Bot(commands.Bot):
    
    def __init__(self):

        super().__init__(token=config.api_key, prefix='?', initial_channels=[val,val2])
        
   

    async def event_message(self, message):

        if message.echo:
            return
        
        print(f'{message.author.display_name}: {message.content}')
        
       
        

        await self.handle_commands(message)

    
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}')



bot = Bot()
bot.run()


